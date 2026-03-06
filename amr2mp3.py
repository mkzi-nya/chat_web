import subprocess
from pathlib import Path
import pilk

AUDIO_DIR = Path("./resources/audios")
CHUNKS_DIR = Path("./code/yiqy/chunks")


def detect_audio_type(path: Path):
    with open(path, "rb") as f:
        head = f.read(16)

    if head.startswith(b"#!AMR"):
        return "amr"

    if b"#!SILK" in head:
        return "silk"

    return "unknown"


def convert_audio():
    converted = []

    for file in AUDIO_DIR.rglob("*.amr"):
        audio_type = detect_audio_type(file)
        mp3 = file.with_suffix(".mp3")

        print(f"[detect] {file.name} -> {audio_type}")

        try:

            if audio_type == "amr":

                subprocess.run(
                    [
                        "ffmpeg",
                        "-y",
                        "-i",
                        str(file),
                        "-acodec",
                        "libmp3lame",
                        "-ab",
                        "128k",
                        str(mp3),
                    ],
                    check=True,
                )

            elif audio_type == "silk":

                pcm = file.with_suffix(".pcm")

                # silk -> pcm
                pilk.decode(str(file), str(pcm))

                # pcm -> mp3
                subprocess.run(
                    [
                        "ffmpeg",
                        "-y",
                        "-f",
                        "s16le",
                        "-ar",
                        "24000",
                        "-ac",
                        "1",
                        "-i",
                        str(pcm),
                        str(mp3),
                    ],
                    check=True,
                )

                pcm.unlink()

            else:
                print(f"[skip] unknown format {file}")
                continue

            if mp3.exists():
                converted.append((file.name, mp3.name))
                print(f"[ok] {file.name} -> {mp3.name}")

        except Exception as e:
            print(f"[fail] {file} : {e}")

    return converted


def replace_in_chunks(converted):

    for file in CHUNKS_DIR.rglob("*"):

        if not file.is_file():
            continue

        try:
            text = file.read_text(encoding="utf-8")
        except:
            continue

        original = text

        for amr, mp3 in converted:
            text = text.replace(amr, mp3)

        if text != original:
            file.write_text(text, encoding="utf-8")
            print(f"[update] {file}")


def main():

    converted = convert_audio()

    replace_in_chunks(converted)

    print("done.")


if __name__ == "__main__":
    main()