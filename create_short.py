"""
YouTube Shorts Creator
Creates a 9:16 vertical video from characters, backgrounds, and story script.
"""
import os
import sys
import textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from moviepy import (
    VideoClip, ImageClip, AudioFileClip, CompositeVideoClip,
    concatenate_videoclips, ColorClip
)
from gtts import gTTS

# --- Constants ---
SHORT_W, SHORT_H = 1080, 1920
FPS = 30
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_PATH_FALLBACK = None  # will use PIL default


# --- Helpers ---
def get_font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except Exception:
        return ImageFont.load_default()


def load_image_rgba(path, target_size=None):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")
    img = Image.open(path).convert("RGBA")
    if target_size:
        img = img.resize(target_size, Image.LANCZOS)
    return img


def fit_background(path, size=(SHORT_W, SHORT_H)):
    """Load and crop/resize image to fill the frame (cover fit)."""
    img = Image.open(path).convert("RGBA")
    img_ratio = img.width / img.height
    target_ratio = size[0] / size[1]
    if img_ratio > target_ratio:
        new_h = size[1]
        new_w = int(new_h * img_ratio)
    else:
        new_w = size[0]
        new_h = int(new_w / img_ratio)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - size[0]) // 2
    top = (new_h - size[1]) // 2
    return img.crop((left, top, left + size[0], top + size[1]))


def place_character(canvas, char_path, position="center", scale=0.5):
    """Paste a character PNG onto the canvas."""
    char = Image.open(char_path).convert("RGBA")
    ch = int(SHORT_H * scale)
    cw = int(char.width * ch / char.height)
    char = char.resize((cw, ch), Image.LANCZOS)

    positions = {
        "left": (SHORT_W // 6 - cw // 2, SHORT_H - ch - 100),
        "center": (SHORT_W // 2 - cw // 2, SHORT_H - ch - 100),
        "right": (5 * SHORT_W // 6 - cw // 2, SHORT_H - ch - 100),
    }
    x, y = positions.get(position, positions["center"])
    canvas.paste(char, (x, y), char)
    return canvas


def draw_text_overlay(canvas, text, position="bottom", font_size=62):
    """Draw styled text with background pill/box."""
    if not text:
        return canvas
    draw = ImageDraw.Draw(canvas)
    font = get_font(font_size)
    max_chars = 28
    lines = []
    for part in text.split("\n"):
        wrapped = textwrap.wrap(part, max_chars) or [""]
        lines.extend(wrapped)

    line_h = font_size + 16
    total_h = line_h * len(lines) + 40
    pad_x = 60

    # Measure max line width
    max_w = max(
        (draw.textbbox((0, 0), ln, font=font)[2] for ln in lines), default=200
    )
    box_w = min(max_w + pad_x * 2, SHORT_W - 80)
    box_x = (SHORT_W - box_w) // 2

    if position == "top":
        box_y = 140
    elif position == "center":
        box_y = (SHORT_H - total_h) // 2
    else:  # bottom
        box_y = SHORT_H - total_h - 140

    # Semi-transparent pill background
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    r = 30
    ov_draw.rounded_rectangle(
        [box_x, box_y, box_x + box_w, box_y + total_h],
        radius=r, fill=(0, 0, 0, 180)
    )
    canvas = Image.alpha_composite(canvas, overlay)
    draw = ImageDraw.Draw(canvas)

    # Draw each line centered
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        lw = bbox[2] - bbox[0]
        lx = (SHORT_W - lw) // 2
        ly = box_y + 20 + i * line_h
        # Shadow
        draw.text((lx + 3, ly + 3), line, fill=(0, 0, 0, 200), font=font)
        draw.text((lx, ly), line, fill=(255, 255, 50), font=font)

    return canvas


def apply_effect_frame(base_frame, effect, t, duration):
    """Apply per-frame visual effects."""
    if effect == "zoom_in":
        scale = 1.0 + 0.08 * (t / duration)
        return zoom_image(base_frame, scale)
    elif effect == "zoom_out":
        scale = 1.08 - 0.08 * (t / duration)
        return zoom_image(base_frame, scale)
    elif effect == "shake":
        if int(t * 10) % 2 == 0:
            return np.roll(base_frame, 8, axis=1)
        return base_frame
    elif effect == "flash":
        brightness = 1.0 + 0.5 * abs(np.sin(t * np.pi * 3))
        frame = (base_frame.astype(np.float32) * brightness).clip(0, 255).astype(np.uint8)
        return frame
    elif effect == "fade_in":
        alpha = min(1.0, t / min(1.0, duration * 0.4))
        return (base_frame.astype(np.float32) * alpha).astype(np.uint8)
    return base_frame


def zoom_image(frame, scale):
    h, w = frame.shape[:2]
    new_w, new_h = int(w * scale), int(h * scale)
    img = Image.fromarray(frame).resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    return np.array(img.crop((left, top, left + w, top + h)))


# --- TTS ---
def make_tts(text, lang, path):
    """Generate TTS audio file."""
    if not text or not text.strip():
        return None
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(path)
        return path
    except Exception as e:
        print(f"  [TTS warning] {e}")
        return None


# --- Scene builder ---
def build_scene_frame(scene):
    """Compose one static PIL frame for a scene."""
    # Background
    if scene.get("background") and os.path.exists(scene["background"]):
        canvas = fit_background(scene["background"])
    else:
        canvas = Image.new("RGBA", (SHORT_W, SHORT_H), (30, 30, 50, 255))

    # Characters
    for char in scene.get("characters", []):
        if os.path.exists(char["image"]):
            canvas = place_character(
                canvas, char["image"],
                position=char.get("position", "center"),
                scale=char.get("scale", 0.5),
            )

    # Text overlay
    canvas = draw_text_overlay(
        canvas,
        scene.get("text", ""),
        position=scene.get("text_position", "bottom"),
    )
    return np.array(canvas.convert("RGB"))


def build_scene_clip(scene, scene_idx, lang):
    """Build a MoviePy clip for one scene."""
    duration = scene.get("duration", 3.0)
    effect = scene.get("effect", "none")
    base_frame = build_scene_frame(scene)

    def make_frame(t):
        return apply_effect_frame(base_frame, effect, t, duration)

    clip = VideoClip(frame_function=make_frame, duration=duration)
    clip = clip.with_fps(FPS)

    # TTS audio
    narration = scene.get("narration", "").strip()
    if narration:
        audio_path = f"assets/audio/scene_{scene_idx}.mp3"
        os.makedirs("assets/audio", exist_ok=True)
        audio_file = make_tts(narration, lang, audio_path)
        if audio_file and os.path.exists(audio_file):
            audio = AudioFileClip(audio_file)
            # Trim audio if longer than scene, or pad scene
            if audio.duration > duration:
                clip = clip.with_duration(audio.duration)
            clip = clip.with_audio(audio)

    return clip


def build_outro_clip(outro_cfg):
    """Simple outro with text on black."""
    duration = outro_cfg.get("duration", 2.5)
    text = outro_cfg.get("text", "")
    canvas = Image.new("RGBA", (SHORT_W, SHORT_H), (10, 10, 10, 255))
    canvas = draw_text_overlay(canvas, text, position="center", font_size=72)
    frame = np.array(canvas.convert("RGB"))
    clip = ImageClip(frame).with_duration(duration).with_fps(FPS)
    return clip


# --- Main ---
def create_youtube_short(story, output_dir="output"):
    print(f"\n{'='*50}")
    print(f"Creating: {story['title']}")
    print(f"{'='*50}\n")

    lang = story.get("language", "vi")
    clips = []

    for i, scene in enumerate(story["scenes"], 1):
        print(f"  Building scene {i}/{len(story['scenes'])}...")
        clip = build_scene_clip(scene, i, lang)
        clips.append(clip)

    if story.get("outro"):
        print("  Building outro...")
        clips.append(build_outro_clip(story["outro"]))

    print("\nConcatenating scenes...")
    final = concatenate_videoclips(clips, method="compose")

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{story.get('output_name', 'short')}.mp4")

    print(f"Rendering to {out_path} ...")
    final.write_videofile(
        out_path,
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="assets/audio/_temp_audio.m4a",
        remove_temp=True,
        logger="bar",
    )
    print(f"\nDone! Video saved: {out_path}")
    print(f"Duration: {final.duration:.1f}s | Size: 1080x1920 (9:16)")
    return out_path


if __name__ == "__main__":
    from story_config import STORY
    create_youtube_short(STORY)
