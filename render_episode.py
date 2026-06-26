"""
Render một tập Hiệp Sĩ Hạt Mít.
Usage: python render_episode.py --season 1 --episode 1
       python render_episode.py --all
"""
import argparse
import os
import sys

from create_short import create_youtube_short
from series_hatmit import SERIES_META, ALL_EPISODES, get_episode


def render_ep(ep_data):
    story = {
        "title": f"[S{ep_data['season']}E{ep_data['episode']:02d}] {ep_data['title']}",
        "language": SERIES_META["language"],
        "output_name": ep_data["output_name"],
        "scenes": ep_data["scenes"],
    }
    if ep_data.get("outro"):
        story["outro"] = ep_data["outro"]

    out_dir = SERIES_META["output_dir"]
    os.makedirs(out_dir, exist_ok=True)

    # Override output dir in create_short
    original_cwd = os.getcwd()
    out_path = create_youtube_short(story, output_dir=out_dir)
    return out_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render Hiệp Sĩ Hạt Mít episodes")
    parser.add_argument("--season", type=int, default=1)
    parser.add_argument("--episode", type=int, default=1)
    parser.add_argument("--all", action="store_true", help="Render all episodes")
    args = parser.parse_args()

    if args.all:
        for ep in ALL_EPISODES:
            print(f"\n{'='*60}")
            print(f"Rendering S{ep['season']}E{ep['episode']:02d}: {ep['title']}")
            render_ep(ep)
    else:
        ep = get_episode(args.season, args.episode)
        if not ep:
            print(f"Episode S{args.season}E{args.episode:02d} not found.")
            sys.exit(1)
        render_ep(ep)
