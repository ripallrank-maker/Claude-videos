"""
Render một tập Hiệp Sĩ Hạt Mít.

Usage:
  python render_episode.py --season 1 --episode 1
  python render_episode.py --season 1 --episode 1 --output /sdcard/Videos
  python render_episode.py --all
  python render_episode.py --all --output /sdcard/Videos/HatMit
"""
import argparse
import os
import sys

from create_short import create_youtube_short
from series_hatmit import SERIES_META, ALL_EPISODES, get_episode


def render_ep(ep_data, output_dir):
    story = {
        "title": f"[S{ep_data['season']}E{ep_data['episode']:02d}] {ep_data['title']}",
        "language": SERIES_META["language"],
        "output_name": ep_data["output_name"],
        "scenes": ep_data["scenes"],
    }
    if ep_data.get("outro"):
        story["outro"] = ep_data["outro"]

    os.makedirs(output_dir, exist_ok=True)
    out_path = create_youtube_short(story, output_dir=output_dir)
    return out_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render Hiệp Sĩ Hạt Mít episodes")
    parser.add_argument("--season", type=int, default=1)
    parser.add_argument("--episode", type=int, default=1)
    parser.add_argument("--all", action="store_true", help="Render tất cả tập đã config")
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Thư mục xuất video (mặc định: output/hatmit). Ví dụ: --output /sdcard/Videos",
    )
    args = parser.parse_args()

    out_dir = args.output if args.output else SERIES_META["output_dir"]

    if args.all:
        for ep in ALL_EPISODES:
            print(f"\n{'='*60}")
            print(f"Rendering S{ep['season']}E{ep['episode']:02d}: {ep['title']}")
            render_ep(ep, out_dir)
        print(f"\nXong! Tất cả video lưu tại: {os.path.abspath(out_dir)}")
    else:
        ep = get_episode(args.season, args.episode)
        if not ep:
            print(f"Không tìm thấy S{args.season}E{args.episode:02d}.")
            sys.exit(1)
        out_path = render_ep(ep, out_dir)
        print(f"\nXong! Video lưu tại: {os.path.abspath(out_path)}")
