"""Generate placeholder test assets when real images aren't available."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1920
CHAR_W, CHAR_H = 400, 600


def text_on_image(img, text, color, font_size=60, pos=None):
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()
    if pos is None:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pos = ((img.width - tw) // 2, (img.height - th) // 2)
    draw.text(pos, text, fill=color, font=font)


def make_background(path, name, base_color, accent_color):
    img = Image.new("RGB", (W, H), base_color)
    draw = ImageDraw.Draw(img)
    # Simple geometric decoration
    for i in range(0, H, 120):
        draw.line([(0, i), (W, i + 60)], fill=accent_color, width=3)
    for i in range(0, W, 120):
        draw.line([(i, 0), (i + 60, H)], fill=accent_color, width=2)
    # Overlay label
    text_on_image(img, name, (255, 255, 255), font_size=80)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print(f"  Created: {path}")


def make_character(path, name, body_color, eye_color=(50, 50, 50)):
    img = Image.new("RGBA", (CHAR_W, CHAR_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Body (rounded rect approximation)
    draw.ellipse([50, 150, 350, 550], fill=body_color)
    # Head
    draw.ellipse([100, 30, 300, 220], fill=body_color)
    # Ears (cat)
    draw.polygon([(100, 80), (60, 10), (140, 70)], fill=body_color)
    draw.polygon([(300, 80), (340, 10), (260, 70)], fill=body_color)
    # Eyes
    draw.ellipse([130, 100, 175, 145], fill=(255, 255, 255))
    draw.ellipse([225, 100, 270, 145], fill=(255, 255, 255))
    draw.ellipse([145, 110, 165, 135], fill=eye_color)
    draw.ellipse([240, 110, 260, 135], fill=eye_color)
    # Nose
    draw.polygon([(195, 155), (185, 170), (215, 170)], fill=(255, 150, 150))
    # Name label
    text_on_image(img, name, (80, 80, 80), font_size=35, pos=(80, 570))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print(f"  Created: {path}")


if __name__ == "__main__":
    print("Generating test assets...")
    make_background("assets/backgrounds/office.jpg", "VĂN PHÒNG", (30, 30, 80), (50, 50, 120))
    make_background("assets/backgrounds/chaos.jpg", "HỖNLOẠN!!!", (120, 20, 20), (180, 40, 40))
    make_character("assets/characters/cat.png", "Mèo Lười", (180, 140, 100))
    print("Done! Test assets ready.")
