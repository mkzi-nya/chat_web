#!/usr/bin/env python3
import sys
import json
from pathlib import Path


def read_jsonl_messages(chunks_dir: Path):
    msgs = {}
    for file in sorted(chunks_dir.glob("chunk_*.jsonl")):
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                obj = json.loads(line)
                msgs[obj["id"]] = obj
    return msgs


def write_chunks(messages, out_dir: Path, max_per_chunk=50000):
    chunks_dir = out_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)

    messages = sorted(messages, key=lambda x: int(x["seq"]))

    chunks_meta = []
    chunk = []
    idx = 1

    def flush(chunk_msgs, idx):
        name = f"chunk_{idx:04d}.jsonl"
        path = chunks_dir / name

        with open(path, "w", encoding="utf-8") as f:
            for m in chunk_msgs:
                f.write(json.dumps(m, ensure_ascii=False) + "\n")

        stat = path.stat()

        chunks_meta.append({
            "index": idx,
            "fileName": name,
            "relativePath": f"chunks/{name}",
            "start": chunk_msgs[0]["time"],
            "end": chunk_msgs[-1]["time"],
            "count": len(chunk_msgs),
            "bytes": stat.st_size
        })

    for m in messages:
        chunk.append(m)
        if len(chunk) >= max_per_chunk:
            flush(chunk, idx)
            chunk = []
            idx += 1

    if chunk:
        flush(chunk, idx)

    return chunks_meta


def rebuild_manifest(manifest_template, messages, chunks_meta):
    manifest = manifest_template

    messages_sorted = sorted(messages, key=lambda x: x["timestamp"])

    manifest["statistics"]["totalMessages"] = len(messages_sorted)
    manifest["statistics"]["timeRange"]["start"] = messages_sorted[0]["time"]
    manifest["statistics"]["timeRange"]["end"] = messages_sorted[-1]["time"]

    manifest["chunked"]["chunks"] = chunks_meta

    return manifest


def main():
    if len(sys.argv) != 4:
        print("usage: python hebk.py path1 path2 output")
        sys.exit(1)

    p1 = Path(sys.argv[1])
    p2 = Path(sys.argv[2])
    out = Path(sys.argv[3])

    out.mkdir(parents=True, exist_ok=True)

    m1 = json.load(open(p1 / "manifest.json", "r", encoding="utf-8"))

    msgs1 = read_jsonl_messages(p1 / "chunks")
    msgs2 = read_jsonl_messages(p2 / "chunks")

    merged = msgs1.copy()

    for mid, msg in msgs2.items():
        if mid not in merged:
            merged[mid] = msg

    messages = list(merged.values())

    chunks_meta = write_chunks(messages, out)

    manifest = rebuild_manifest(m1, messages, chunks_meta)

    with open(out / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()