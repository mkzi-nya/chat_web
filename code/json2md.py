import os
import json
import glob
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from collections import defaultdict
from multiprocessing import Pool, Lock, cpu_count
from bisect import bisect_left
import html
import sys
import time


# ==============================
# 类型转换工具
# ==============================

def to_int(v, default=0):
    if v is None:
        return default

    v = str(v).strip()

    if v.lower() in ["none", "null", ""]:
        return default

    return int(v)


def to_str(v):
    if v is None:
        return ""

    v = str(v).strip()

    if v.lower() in ["none", "null"]:
        return ""

    return v


def to_list(v):
    if v is None:
        return []

    v = str(v).strip()

    if v.lower() in ["none", "null", ""]:
        return []

    return [x.strip() for x in v.split(",") if x.strip()]


# ==============================
# CONFIG
# ==============================

def create_default_config(path="config.json"):
    cfg = {
        "paths": {
            "dataset_root": "./dataset",
            "output_dir": "./vite/chat_vitepress/docs/chat",
            "vitepress_config": "./vite/chat_vitepress/docs/.vitepress/config.js"
        },

        "identity": {
            "who_am_i": "None"
        },

        "resource": {
            "base_url": "https://mkzi-nya.github.io/awa/main/nwf/resources",
            "image_path": "images",
            "video_path": "videos",
            "audio_path": "audios",
            "file_path": "file"
        },

        "time": {
            "timezone_offset_hours": "8",
            "time_gap_seconds": "300"
        },

        "render": {
            "markdown_escape_chars": "\\`*_{}[]()#+-.!",
            "newline_replace": "<br>"
        },

        "media": {
            "video_extensions": "mp4,webm,mkv",
            "audio_extensions": "mp3,wav,flac,ogg"
        },

        "parallel": {
            "max_workers": "8"
        },

        "sidebar": {
            "chat_title": "聊天记录",
            "chat_route": "/chat/",
            "target_group": "None"
        },

        "avatar": {
            "qq_avatar_url": "https://q.qlogo.cn/g?b=qq&nk={uin}&s=100"
        }
    }

    with open(path, "w", encoding="utf8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)

    print("config.json 已生成")


def load_config():
    if len(sys.argv) < 2:
        print("Usage: python 1.py config.json")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "config":
        create_default_config()
        sys.exit(0)

    if not os.path.exists(arg):
        print(f"配置文件不存在: {arg}")
        sys.exit(1)

    if os.path.isdir(arg):
        print(f"传入的是目录，不是配置文件: {arg}")
        sys.exit(1)

    with open(arg, "r", encoding="utf8") as f:
        return json.load(f)


config = load_config()


# ==============================
# PATHS
# ==============================

DATASET_ROOT = to_str(config["paths"]["dataset_root"])

MANIFEST = os.path.join(DATASET_ROOT, "manifest.json")
CHUNK_DIR = os.path.join(DATASET_ROOT, "chunks")

OUT_DIR = to_str(config["paths"]["output_dir"])
VITEPRESS_CONFIG = to_str(config["paths"]["vitepress_config"])

if not os.path.exists(MANIFEST):
    print(f"manifest.json 不存在: {MANIFEST}")
    sys.exit(1)

if not os.path.isdir(CHUNK_DIR):
    print(f"chunks 目录不存在: {CHUNK_DIR}")
    sys.exit(1)


# ==============================
# RESOURCE
# ==============================

RESOURCE_BASE = to_str(config["resource"]["base_url"])

IMG_PATH = to_str(config["resource"]["image_path"])
VIDEO_PATH = to_str(config["resource"]["video_path"])
AUDIO_PATH = to_str(config["resource"]["audio_path"])
FILE_PATH = to_str(config["resource"]["file_path"])


# ==============================
# TIME
# ==============================

TIME_GAP = to_int(config["time"]["time_gap_seconds"])

UTC = timezone(
    timedelta(hours=to_int(config["time"]["timezone_offset_hours"]))
)


# ==============================
# RENDER
# ==============================

ESCAPE_CHARS = to_str(config["render"]["markdown_escape_chars"])
NEWLINE_REPLACE = to_str(config["render"]["newline_replace"])


# ==============================
# MEDIA
# ==============================

VIDEO_EXT = set(to_list(config["media"]["video_extensions"]))
AUDIO_EXT = set(to_list(config["media"]["audio_extensions"]))


# ==============================
# PARALLEL
# ==============================

MAX_WORKERS = to_int(config["parallel"]["max_workers"], 8)
if MAX_WORKERS <= 0:
    MAX_WORKERS = 1


# ==============================
# AVATAR
# ==============================

AVATAR_TEMPLATE = to_str(config["avatar"]["qq_avatar_url"])


# ==============================
# SIDEBAR
# ==============================

SIDEBAR_TITLE = to_str(config["sidebar"]["chat_title"])
SIDEBAR_ROUTE = to_str(config["sidebar"]["chat_route"])
SIDEBAR_TARGET = to_str(config["sidebar"].get("target_group"))

lock = Lock()


# ==============================
# MANIFEST
# ==============================

with open(MANIFEST, "r", encoding="utf8") as f:
    manifest = json.load(f)

config_uid = to_str(config["identity"]["who_am_i"])

if config_uid:
    self_uid = config_uid
else:
    self_uid = str(manifest["chatInfo"]["selfUid"])

uid_name_map = {}
for s in manifest["statistics"]["senders"]:
    uid_name_map[str(s["uid"])] = s["name"]


# ==============================
# UTIL
# ==============================

def escape_text(t):
    if not t:
        return ""

    t = str(t)
    t = html.escape(t)

    for c in ESCAPE_CHARS:
        t = t.replace(c, "\\" + c)

    return t.replace("\n", NEWLINE_REPLACE)


def avatar(uin):
    return AVATAR_TEMPLATE.format(uin=uin)


def dt(ts):
    return datetime.fromtimestamp(ts / 1000, tz=UTC)


def hour_anchor(ts):
    h = dt(ts).strftime("%H")

    return f"""
## <span class="hidden-title">{h}:00</span> <a id="{h}:00"></a>
"""


def render_time(ts):
    t = dt(ts).strftime("%H:%M")

    return f"""
<ChatBubble role="system">
{t}
</ChatBubble>
"""


# ==============================
# REPLY
# ==============================

def resolve_reply_target(reply_ts, timeline):
    if reply_ts is None:
        return None

    reply_ts = int(reply_ts * 1000)

    idx = bisect_left(timeline, reply_ts)

    if idx == 0:
        return None

    if idx >= len(timeline):
        return len(timeline) - 1

    return idx - 1 if timeline[idx] != reply_ts else idx


def render_reply(data, timeline, msgs):
    reply_ts = data.get("timestamp")

    idx = resolve_reply_target(reply_ts, timeline)

    msg_id = None

    if idx is not None and 0 <= idx < len(msgs):
        msg_id = msgs[idx].get("id")

    sender = escape_text(data.get("senderName", ""))
    content = escape_text(data.get("content", ""))

    time_str = ""

    if reply_ts:
        try:
            time_str = datetime.fromtimestamp(float(reply_ts), tz=UTC).strftime("%H:%M")
        except:
            try:
                time_str = dt(int(float(reply_ts) * 1000)).strftime("%H:%M")
            except:
                pass

    return f"""
<div class="reply-box" data-target="msg_{msg_id}">
<div class="reply-header">{sender} {time_str}</div>
<div class="reply-text">{content}</div>
</div>
"""


# ==============================
# SYSTEM / GRAYTIP
# ==============================

def parse_gtip(xml_text):
    try:
        root = ET.fromstring(xml_text)
    except:
        return None

    parts = []

    for node in root:
        tag = node.tag

        if tag == "qq":
            uid = str(node.attrib.get("uin", ""))
            parts.append(uid_name_map.get(uid, uid))

        elif tag == "nor":
            parts.append(node.attrib.get("txt", ""))

        elif tag == "url":
            parts.append(node.attrib.get("txt", ""))

    parts = [p for p in parts if p]

    if parts:
        return " ".join(parts)

    return None


def parse_json_graytip(json_str):
    try:
        data = json.loads(json_str)
    except:
        return None

    parts = []

    for item in data.get("items", []):
        tp = item.get("type")

        if tp == "qq":
            uid = str(item.get("uid", ""))
            parts.append(uid_name_map.get(uid, uid))

        elif tp == "nor":
            parts.append(item.get("txt", ""))

        elif tp == "url":
            parts.append(item.get("txt", ""))

    parts = [p for p in parts if p]

    if parts:
        return " ".join(parts)

    return None


def render_system(msg):

    content = msg.get("content", {})
    elements = content.get("elements", [])

    for el in elements:

        if el.get("type") != "system":
            continue

        data = el.get("data", {})
        original = data.get("originalData", {})

        # =========================
        # 撤回消息
        # =========================

        revoke = original.get("revokeElement")

        if revoke and msg.get("recalled"):

            wording = escape_text(
                revoke.get("wording")
                or data.get("text")
                or content.get("text")
                or ""
            )

            who = "你" if revoke.get("isSelfOperate") else "对方"

            return f"""
<ChatBubble role="system">
{who}撤回了一条消息，{wording}
</ChatBubble>
"""

        # =========================
        # 文件接收提示
        # =========================

        file_receipt = original.get("fileReceiptElement")

        if file_receipt:

            filename = escape_text(file_receipt.get("fileName"))

            if filename:
                return f"""
<ChatBubble role="system">
对方已接受 {filename}
</ChatBubble>
"""

        # =========================
        # XML graytip
        # =========================

        xml = original.get("xmlElement")

        if xml and xml.get("content"):

            try:

                root = ET.fromstring(xml.get("content"))

                parts = []

                # 兼容 <gtip><nor>...</nor></gtip>
                for node in root.iter():

                    tag = node.tag

                    if tag == "qq":

                        uid = str(node.attrib.get("uin", ""))

                        parts.append(uid_name_map.get(uid, uid))

                    elif tag == "nor":

                        parts.append(node.attrib.get("txt") or node.text or "")

                    elif tag == "url":

                        parts.append(node.attrib.get("txt", ""))

                parts = [p for p in parts if p]

                if parts:

                    parsed = " ".join(parts)

                    return f"""
<ChatBubble role="system">
{escape_text(parsed)}
</ChatBubble>
"""

            except:
                pass

        # =========================
        # JSON graytip
        # =========================

        gray = original.get("jsonGrayTipElement")

        if gray and gray.get("jsonStr"):

            parsed = parse_json_graytip(gray.get("jsonStr"))

            if parsed:
                return f"""
<ChatBubble role="system">
{escape_text(parsed)}
</ChatBubble>
"""

        # =========================
        # fallback
        # =========================

        txt = data.get("summary") or data.get("text") or content.get("text")

        if txt:

            return f"""
<ChatBubble role="system">
{escape_text(txt)}
</ChatBubble>
"""

    return None

# ==============================
# MEDIA RENDER
# ==============================

def render_file(data):
    filename = data.get("filename")

    if not filename:
        return ""

    filename_safe = escape_text(filename)
    url = f"{RESOURCE_BASE}/{FILE_PATH}/{filename}"

    ext = filename.lower().split(".")[-1]

    if ext in VIDEO_EXT:
        return f"""
<video controls class="chat-video">
<source src="{RESOURCE_BASE}/{VIDEO_PATH}/{filename}">
</video>
"""

    if ext in AUDIO_EXT:
        return f"""
<audio controls class="chat-audio">
<source src="{RESOURCE_BASE}/{AUDIO_PATH}/{filename}">
</audio>
"""

    return f'<a href="{url}" download class="chat-file">📄 {filename_safe}</a>'


def render_audio(data):
    filename = data.get("filename")

    if not filename:
        return ""

    url = f"{RESOURCE_BASE}/{AUDIO_PATH}/{filename}"

    return f"""
<audio controls class="chat-audio">
<source src="{url}">
</audio>
"""


# ==============================
# MESSAGE RENDER
# ==============================

def render_message(msg, timeline, msgs):

    if msg.get("type") == "system":
        return render_system(msg)

    sender = msg.get("sender", {})

    uin = str(sender.get("uin", ""))
    uid = str(sender.get("uid", ""))

    role = "me" if (uin == self_uid or uid == self_uid) else "user"

    msg_id = msg.get("id")

    parts = []

    elements = (msg.get("content") or {}).get("elements", [])

    for el in elements:

        tp = el.get("type")
        data = el.get("data", {}) or {}

        if tp == "text":

            parts.append(escape_text(data.get("text")))

        elif tp == "image":

            fn = data.get("filename")

            if fn:

                parts.append(
                    f'<img src="{RESOURCE_BASE}/{IMG_PATH}/{fn}">'
                )

        elif tp == "file":

            parts.append(render_file(data))

        elif tp == "audio":

            parts.append(render_audio(data))

        elif tp == "reply":

            parts.append(render_reply(data, timeline, msgs))

    body = "<br>".join([p for p in parts if p])

    return f"""
<ChatBubble role="{role}" avatar="{avatar(uin)}" id="msg_{msg_id}">
{body}
</ChatBubble>
"""

# ==============================
# PARSER
# ==============================

def parse_chunk(path):
    out = []

    with open(path, "r", encoding="utf8") as fp:
        for line in fp:
            line = line.strip()

            if not line:
                continue

            try:
                out.append(json.loads(line))
            except:
                pass

    with lock:
        print(f"读取 {os.path.basename(path)} 完成 ({len(out)})")

    return out


# ==============================
# SIDEBAR
# ==============================

def build_sidebar_tree():
    tree = defaultdict(lambda: defaultdict(list))

    for root, dirs, files in os.walk(OUT_DIR):
        for f in files:
            if not f.endswith(".md"):
                continue

            rel = os.path.relpath(os.path.join(root, f), OUT_DIR)
            parts = rel.replace("\\", "/").split("/")

            if len(parts) != 3:
                continue

            y, m, dfile = parts
            d = dfile.replace(".md", "")

            tree[y][m].append(d)

    years = sorted(tree.keys())

    sidebar = []

    for y in years:
        months = sorted(tree[y].keys())
        month_items = []

        for m in months:
            days = sorted(tree[y][m])

            day_items = []
            for d in days:
                day_items.append(
                    f"{{text:'{d}',link:'{SIDEBAR_ROUTE}{y}/{m}/{d}'}}"
                )

            month_items.append(
                f"{{text:'{m}',collapsed:true,items:[{','.join(day_items)}]}}"
            )

        sidebar.append(
            f"{{text:'{y}',collapsed:true,items:[{','.join(month_items)}]}}"
        )

    return "[" + ",".join(sidebar) + "]"


def write_sidebar_config():
    if not VITEPRESS_CONFIG:
        return

    if not os.path.exists(VITEPRESS_CONFIG):
        print(f"vitepress config 不存在: {VITEPRESS_CONFIG}")
        return

    with open(VITEPRESS_CONFIG, "r", encoding="utf8") as f:
        config_text = f.read()

    target = SIDEBAR_TARGET if SIDEBAR_TARGET else SIDEBAR_TITLE

    pos = config_text.find(f"text: '{target}'")
    if pos == -1:
        pos = config_text.find(f'text: "{target}"')

    if pos == -1:
        print("未找到 sidebar 目标")
        return

    items_pos = config_text.find("items:", pos)
    if items_pos == -1:
        print("未找到目标 items")
        return

    start_bracket = config_text.find("[", items_pos)
    if start_bracket == -1:
        print("未找到 items 数组起始位置")
        return

    depth = 0
    end_bracket = None

    for i in range(start_bracket, len(config_text)):
        ch = config_text[i]

        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                end_bracket = i + 1
                break

    if end_bracket is None:
        print("未找到 items 数组结束位置")
        return

    new_items = build_sidebar_tree()
    new_config = config_text[:start_bracket] + new_items + config_text[end_bracket:]

    with open(VITEPRESS_CONFIG, "w", encoding="utf8") as f:
        f.write(new_config)

    print("✔ sidebar 已更新")


# ==============================
# MAIN
# ==============================

def main():
    files = sorted(glob.glob(os.path.join(CHUNK_DIR, "*.jsonl")))

    if not files:
        print(f"未找到 chunk 文件: {CHUNK_DIR}")
        sys.exit(1)

    workers = min(cpu_count(), MAX_WORKERS)
    print(f"使用 {workers} 进程解析")

    with Pool(workers) as p:
        results = p.map(parse_chunk, files)

    msgs = []

    for r in results:
        msgs.extend(r)

    msgs.sort(key=lambda x: x.get("timestamp", 0))

    timeline = [m.get("timestamp", 0) for m in msgs]

    total = len(msgs)
    by_day = defaultdict(list)

    last_ts = None
    last_hour = None

    start_time = time.time()

    for i, m in enumerate(msgs):
        ts = int(m.get("timestamp", 0))
        d = dt(ts)

        y = d.strftime("%Y")
        mo = d.strftime("%m")
        da = d.strftime("%d")

        key = f"{y}/{mo}/{da}"
        hour = d.strftime("%H")

        if hour != last_hour:
            by_day[key].append(hour_anchor(ts))
            by_day[key].append(render_time(ts))
            last_hour = hour

        elif last_ts and (ts - last_ts) / 1000 >= TIME_GAP:
            by_day[key].append(render_time(ts))

        html_msg = render_message(m, timeline, msgs)

        if html_msg:
            by_day[key].append(html_msg)

        last_ts = ts

        if total > 0 and i % 5000 == 0:
            pct = i / total * 100
            sys.stdout.write(f"\r生成进度 {pct:.1f}%")
            sys.stdout.flush()

    print("\n写入文件")

    for k, v in by_day.items():
        path = os.path.join(OUT_DIR, f"{k}.md")

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf8") as f:
            f.write("\n".join(v))

        print("✔", path)

    write_sidebar_config()

    print(f"完成 用时 {time.time() - start_time:.2f}s")


if __name__ == "__main__":
    main()