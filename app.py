"""
Hiệp Sĩ Hạt Mít — Web App
Mobile-friendly web interface để render và tải video Shorts.
"""
import os
import threading
import time
from flask import Flask, render_template, jsonify, send_file, request
from series_hatmit import ALL_EPISODES, SERIES_META, get_episode
from create_short import create_youtube_short

app = Flask(__name__)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output", "hatmit")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Track render jobs: { job_id: { status, progress, message, file } }
jobs = {}


def run_render(job_id, ep_data):
    jobs[job_id] = {"status": "running", "progress": 0, "message": "Đang chuẩn bị...", "file": None}
    try:
        story = {
            "title": f"[S{ep_data['season']}E{ep_data['episode']:02d}] {ep_data['title']}",
            "language": SERIES_META["language"],
            "output_name": ep_data["output_name"],
            "scenes": ep_data["scenes"],
        }
        if ep_data.get("outro"):
            story["outro"] = ep_data["outro"]

        total = len(story["scenes"]) + (1 if story.get("outro") else 0)

        # Patch progress reporting into scene building
        from create_short import (
            build_scene_clip, build_outro_clip, concatenate_videoclips, FPS
        )

        clips = []
        for i, scene in enumerate(story["scenes"], 1):
            pct = int((i - 1) / total * 70)
            jobs[job_id]["progress"] = pct
            jobs[job_id]["message"] = f"Dựng cảnh {i}/{len(story['scenes'])}..."
            clips.append(build_scene_clip(scene, i, story["language"]))

        if story.get("outro"):
            jobs[job_id]["progress"] = 72
            jobs[job_id]["message"] = "Dựng outro..."
            clips.append(build_outro_clip(story["outro"]))

        jobs[job_id]["progress"] = 75
        jobs[job_id]["message"] = "Ghép cảnh..."
        final = concatenate_videoclips(clips, method="compose")

        out_path = os.path.join(OUTPUT_DIR, f"{story['output_name']}.mp4")
        jobs[job_id]["progress"] = 80
        jobs[job_id]["message"] = "Đang render video (vui lòng chờ)..."

        final.write_videofile(
            out_path,
            fps=FPS,
            codec="libx264",
            audio_codec="aac",
            temp_audiofile=os.path.join(OUTPUT_DIR, "_temp.m4a"),
            remove_temp=True,
            logger=None,
        )

        jobs[job_id]["progress"] = 100
        jobs[job_id]["status"] = "done"
        jobs[job_id]["message"] = "Xong!"
        jobs[job_id]["file"] = out_path

    except Exception as e:
        jobs[job_id]["status"] = "error"
        jobs[job_id]["message"] = f"Lỗi: {str(e)}"


@app.route("/")
def index():
    episodes = []
    for ep in ALL_EPISODES:
        out_path = os.path.join(OUTPUT_DIR, f"{ep['output_name']}.mp4")
        episodes.append({
            "season": ep["season"],
            "episode": ep["episode"],
            "title": ep["title"],
            "youtube_title": ep.get("youtube_title", ep["title"]),
            "output_name": ep["output_name"],
            "rendered": os.path.exists(out_path),
            "file_size": f"{os.path.getsize(out_path) / 1024 / 1024:.1f} MB" if os.path.exists(out_path) else None,
        })
    return render_template("index.html", episodes=episodes, series=SERIES_META)


@app.route("/render/<output_name>", methods=["POST"])
def render(output_name):
    ep = next((e for e in ALL_EPISODES if e["output_name"] == output_name), None)
    if not ep:
        return jsonify({"error": "Không tìm thấy tập"}), 404

    job_id = output_name
    if job_id in jobs and jobs[job_id]["status"] == "running":
        return jsonify({"error": "Đang render rồi"}), 409

    thread = threading.Thread(target=run_render, args=(job_id, ep), daemon=True)
    thread.start()
    return jsonify({"job_id": job_id})


@app.route("/status/<job_id>")
def status(job_id):
    if job_id not in jobs:
        out_path = os.path.join(OUTPUT_DIR, f"{job_id}.mp4")
        if os.path.exists(out_path):
            return jsonify({"status": "done", "progress": 100, "message": "Sẵn sàng tải"})
        return jsonify({"status": "idle", "progress": 0, "message": ""})
    return jsonify(jobs[job_id])


@app.route("/download/<output_name>")
def download(output_name):
    path = os.path.join(OUTPUT_DIR, f"{output_name}.mp4")
    if not os.path.exists(path):
        return "File không tồn tại", 404
    return send_file(path, as_attachment=True, download_name=f"{output_name}.mp4")


if __name__ == "__main__":
    print("🌱 Hiệp Sĩ Hạt Mít Web App")
    print("   Mở trình duyệt: http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
