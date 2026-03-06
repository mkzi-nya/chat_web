#!/data/data/com.termux/files/usr/bin/python

import os
import sys
import shutil
import json

BASE = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser("~")

SRC = os.path.join(BASE, "chat_vitepress")
DST = os.path.join(HOME, "chat_vitepress")

DOCS = os.path.join(DST, "docs")
TMP = os.path.join(DST, "tmp")

OUTPUT = os.path.join(BASE, "awa/main/nwf")

BATCH_LIMIT = 100 * 1024 * 1024


def ensure(p):
    os.makedirs(p, exist_ok=True)


def run(cmd):
    if os.system(cmd) != 0:
        sys.exit(1)


def filesize(p):
    return os.path.getsize(p)


def loadjson(p):
    if not os.path.exists(p):
        return {}
    with open(p, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}


def savejson(p, d):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, separators=(",", ":"))


# ------------------------------------------------
# 同步 vitepress（低内存逐文件复制）
# ------------------------------------------------

def sync(selected):

    ensure(DST)

    for item in os.listdir(SRC):

        if item == "docs":
            continue

        s = os.path.join(SRC, item)
        d = os.path.join(DST, item)

        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            ensure(os.path.dirname(d))
            shutil.copy2(s, d)

    source_docs = os.path.join(SRC, "docs")

    ensure(DOCS)

    if selected:
        shutil.rmtree(DOCS)
        shutil.copytree(os.path.join(source_docs, selected), DOCS)
    else:
        shutil.copytree(source_docs, DOCS, dirs_exist_ok=True)


# ------------------------------------------------
# rebuild tmp
# ------------------------------------------------

def rebuild_tmp():

    if os.path.exists(TMP):
        shutil.rmtree(TMP)

    ensure(TMP)

    for root, _, files in os.walk(DOCS):

        for f in files:

            if not f.endswith(".md"):
                continue

            if f == "index.md":
                continue

            src = os.path.join(root, f)
            rel = os.path.relpath(src, DOCS)

            dst = os.path.join(TMP, rel)

            ensure(os.path.dirname(dst))

            shutil.move(src, dst)


# ------------------------------------------------
# tmp 统计
# ------------------------------------------------

def count_tmp():

    count = 0

    for _, _, files in os.walk(TMP):
        count += len(files)

    return count


# ------------------------------------------------
# docs 是否有 md
# ------------------------------------------------

def docs_has_md():

    for root, _, files in os.walk(DOCS):

        for f in files:

            if f.endswith(".md") and f != "index.md":
                return True

    return False


# ------------------------------------------------
# 低内存 batch
# ------------------------------------------------

def move_batch():

    size = 0
    moved = 0

    for root, _, files in os.walk(TMP):

        for f in files:

            src = os.path.join(root, f)
            rel = os.path.relpath(src, TMP)

            s = filesize(src)

            if s > BATCH_LIMIT and moved == 0:

                dst = os.path.join(DOCS, rel)
                ensure(os.path.dirname(dst))
                shutil.move(src, dst)

                return 1

            if size + s > BATCH_LIMIT:
                return moved

            dst = os.path.join(DOCS, rel)

            ensure(os.path.dirname(dst))

            shutil.move(src, dst)

            size += s
            moved += 1

    return moved


# ------------------------------------------------
# build
# ------------------------------------------------

def build():

    os.chdir(DST)

    os.environ["NODE_OPTIONS"] = "--max-old-space-size=4096"

    run("pnpm exec vitepress build docs")


# ------------------------------------------------
# dist复制
# ------------------------------------------------

def merge_hashmap(dist):

    src = os.path.join(dist, "hashmap.json")
    dst = os.path.join(OUTPUT, "hashmap.json")

    new = loadjson(src)
    old = loadjson(dst)

    old.update(new)

    savejson(dst, old)


def copy_dist():

    dist = os.path.join(DST, "docs/.vitepress/dist")

    ensure(OUTPUT)

    for root, _, files in os.walk(dist):

        for f in files:

            if f.endswith(".html"):

                src = os.path.join(root, f)
                rel = os.path.relpath(src, dist)

                dst = os.path.join(OUTPUT, rel)

                ensure(os.path.dirname(dst))

                shutil.copy2(src, dst)

    src_assets = os.path.join(dist, "assets")
    dst_assets = os.path.join(OUTPUT, "assets")

    ensure(dst_assets)

    for root, _, files in os.walk(src_assets):

        rel = os.path.relpath(root, src_assets)
        target = os.path.join(dst_assets, rel)

        ensure(target)

        for f in files:

            s = os.path.join(root, f)
            d = os.path.join(target, f)

            if not os.path.exists(d):
                shutil.copy2(s, d)

    merge_hashmap(dist)


# ------------------------------------------------
# 清理 docs
# ------------------------------------------------

def clear_docs():

    for root, dirs, files in os.walk(DOCS):

        dirs[:] = [d for d in dirs if d != ".vitepress"]

        for f in files:

            if not f.endswith(".md"):
                continue

            if f == "index.md":
                continue

            os.remove(os.path.join(root, f))


# ------------------------------------------------
# main
# ------------------------------------------------

def main():

    args = sys.argv[1:]

    cont = "--c" in args
    args = [a for a in args if a != "--c"]

    selected = args[0] if args else None

    if not cont:

        sync(selected)

        os.chdir(DST)

        run("pnpm install --prefer-offline")

        rebuild_tmp()

    ensure(DOCS)
    ensure(TMP)

    while True:

        if docs_has_md():

            build()
            copy_dist()
            clear_docs()

        elif count_tmp() > 0:

            if move_batch() == 0:
                break

        else:
            break

        print(f"remaining: {count_tmp()}")


if __name__ == "__main__":
    main()