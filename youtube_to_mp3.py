#!/usr/bin/env python3

import argparse
import shutil
from pathlib import Path

import yt_dlp


def main():
    parser = argparse.ArgumentParser(
        description="Convert YouTube URLs from a text file to MP3."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Text file containing one YouTube URL per line",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("downloads"),
        help="Output directory (default: downloads)",
    )
    parser.add_argument(
        "-q",
        "--quality",
        choices=("128", "192", "256", "320"),
        default="192",
        help="MP3 bitrate in kbps (default: 192)",
    )
    args = parser.parse_args()

    if not args.input_file.is_file():
        raise SystemExit(f"Input file not found: {args.input_file}")

    if shutil.which("ffmpeg") is None:
        raise SystemExit(
            "FFmpeg is not installed or is not available on PATH."
        )

    urls = [
        line.strip()
        for line in args.input_file.read_text(
            encoding="utf-8-sig"
        ).splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]

    if not urls:
        raise SystemExit("The input file contains no URLs.")

    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(
            output_dir / "%(title)s [%(id)s].%(ext)s"
        ),
        "noplaylist": True,
        "windowsfilenames": True,
        "ignoreerrors": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": args.quality,
            },
            {
                "key": "FFmpegMetadata",
                "add_metadata": True,
            },
        ],
    }

    print(f"Found {len(urls)} URL(s).")
    print(f"Saving MP3 files to: {output_dir}")

    with yt_dlp.YoutubeDL(options) as downloader:
        downloader.download(urls)

    print("Finished.")


if __name__ == "__main__":
    main()