"""Generate folk-art style placeholder assets for Hiệp Sĩ Hạt Mít series."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1920


def font(size):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except Exception:
        return ImageFont.load_default()


def make_bg(path, name, colors, lines=True):
    img = Image.new("RGB", (W, H), colors[0])
    draw = ImageDraw.Draw(img)
    if lines:
        for i in range(0, H, 80):
            draw.line([(0, i), (W, i + 40)], fill=colors[1], width=2)
        for i in range(0, W, 80):
            draw.line([(i, 0), (i + 40, H)], fill=colors[1], width=2)
    # Vignette-like border
    for j in range(40):
        alpha = int(60 * (1 - j / 40))
        draw.rectangle([j, j, W - j, H - j], outline=(*colors[2], alpha), width=1)
    f = font(70)
    bbox = draw.textbbox((0, 0), name, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((W - tw) // 2 + 3, (H - th) // 2 + 3), name, fill=(0, 0, 0, 120), font=f)
    draw.text(((W - tw) // 2, (H - th) // 2), name, fill=(255, 240, 200), font=f)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img.save(path)
    print(f"  BG: {path}")


def oval(draw, cx, cy, rx, ry, fill, outline=None, width=3):
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=fill, outline=outline, width=width)


def make_mit_coi(path):
    """Hạt mít tròn, bóng, nhỏ, có mặt dễ thương."""
    img = Image.new("RGBA", (400, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    body_color = (180, 140, 80)
    outline_color = (100, 70, 30)
    # Áo choàng lá chuối
    draw.polygon([(60, 280), (200, 200), (340, 280), (320, 480), (80, 480)],
                 fill=(60, 140, 60), outline=(30, 90, 30), width=3)
    # Thân hạt mít (oval)
    oval(draw, 200, 300, 130, 145, body_color, outline_color, 5)
    # Texture vỏ mít (gai nhỏ)
    for i in range(8):
        angle_x = 100 + i * 30
        draw.ellipse([angle_x, 175, angle_x + 8, 190], fill=outline_color)
    # Mặt
    oval(draw, 200, 270, 80, 75, (220, 180, 110), outline_color, 4)
    # Mắt
    oval(draw, 170, 255, 20, 22, (255, 255, 255))
    oval(draw, 230, 255, 20, 22, (255, 255, 255))
    oval(draw, 174, 259, 12, 13, (60, 40, 20))
    oval(draw, 234, 259, 12, 13, (60, 40, 20))
    oval(draw, 178, 261, 5, 5, (255, 255, 255))
    oval(draw, 238, 261, 5, 5, (255, 255, 255))
    # Miệng cười
    draw.arc([175, 270, 225, 295], start=10, end=170, fill=outline_color, width=4)
    # Má ửng hồng
    oval(draw, 150, 278, 15, 10, (255, 180, 160, 150))
    oval(draw, 250, 278, 15, 10, (255, 180, 160, 150))
    # Tay cầm gai kiếm
    draw.line([(340, 330), (390, 220)], fill=(140, 110, 60), width=8)
    draw.line([(390, 220), (395, 160)], fill=(200, 200, 100), width=5)
    draw.ellipse([385, 155, 405, 175], fill=(220, 220, 80), outline=(160, 160, 40), width=2)
    # Chân tròn
    oval(draw, 155, 455, 40, 25, body_color, outline_color, 3)
    oval(draw, 245, 455, 40, 25, body_color, outline_color, 3)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img.save(path)
    print(f"  Char: {path}")


def make_cua_kep_cat(path):
    """Cua biển to, đỏ, hay cà khịa."""
    img = Image.new("RGBA", (500, 450), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    body = (200, 60, 30)
    dark = (130, 30, 10)
    # Mai cua (hình bầu dục dẹt)
    oval(draw, 250, 260, 160, 110, body, dark, 5)
    # Mắt trên cuống
    for ex, ey in [(160, 170), (340, 170)]:
        draw.line([(ex, ey + 20), (ex, ey + 70)], fill=dark, width=8)
        oval(draw, ex, ey + 15, 22, 22, (255, 255, 255), dark, 3)
        oval(draw, ex, ey + 15, 12, 12, (40, 40, 40))
    # Càng
    for side, flip in [(-1, 0), (1, 320)]:
        cx, cy = flip + 90 * (1 - flip // 160), 220
        pts = [
            (90 + flip * 0, 250),
            (20 + flip * 0, 180),
            (10 + flip * 0, 130),
            (40 + flip * 0, 110),
            (80 + flip * 0, 150),
        ]
        # Simplified
    # Left claw
    draw.polygon([(90, 250), (20, 195), (10, 140), (50, 120), (80, 175)],
                 fill=body, outline=dark, width=4)
    draw.ellipse([5, 95, 55, 125], fill=dark)
    # Right claw
    draw.polygon([(410, 250), (480, 195), (490, 140), (450, 120), (420, 175)],
                 fill=body, outline=dark, width=4)
    draw.ellipse([445, 95, 495, 125], fill=dark)
    # Chân bên
    for cx in [130, 160, 340, 370]:
        draw.line([(cx, 340), (cx - 20, 410)], fill=dark, width=6)
    # Miệng bong bóng
    draw.arc([190, 295, 310, 330], start=185, end=355, fill=(255, 220, 200), width=5)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img.save(path)
    print(f"  Char: {path}")


def make_thay_vo_san(path):
    """Hạt mít cổ đại, nhăn, râu rễ, mắt lim dim."""
    img = Image.new("RGBA", (400, 620), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    old_body = (140, 100, 55)
    wrinkle = (90, 60, 25)
    robe = (80, 60, 30)
    # Áo choàng rễ cây
    draw.polygon([(50, 280), (200, 220), (350, 280), (370, 590), (30, 590)],
                 fill=robe, outline=wrinkle, width=4)
    # Các đường nhăn áo
    for y in range(320, 580, 40):
        draw.line([(60, y), (340, y + 20)], fill=wrinkle, width=2)
    # Thân (dẹt hơn, già hơn)
    oval(draw, 200, 310, 120, 130, old_body, wrinkle, 5)
    # Nhăn trên vỏ
    for i in range(5):
        draw.arc([100 + i * 15, 240 + i * 12, 290 - i * 10, 340 + i * 10],
                 start=200, end=340, fill=wrinkle, width=2)
    # Mặt (oval nhỏ, già)
    oval(draw, 200, 280, 75, 70, (175, 130, 75), wrinkle, 4)
    # Mắt lim dim
    draw.arc([148, 258, 188, 278], start=0, end=180, fill=wrinkle, width=5)
    draw.arc([212, 258, 252, 278], start=0, end=180, fill=wrinkle, width=5)
    # Râu rễ
    for rx, ry, ex, ey in [(165, 305, 100, 370), (190, 310, 155, 380),
                            (210, 310, 210, 385), (225, 305, 265, 378),
                            (240, 300, 310, 365)]:
        draw.line([(rx, ry), (ex, ey)], fill=wrinkle, width=4)
        draw.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill=wrinkle)
    # Gậy rễ cây
    draw.line([(340, 300), (380, 580)], fill=wrinkle, width=12)
    draw.ellipse([365, 565, 400, 595], fill=old_body, outline=wrinkle, width=3)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img.save(path)
    print(f"  Char: {path}")


def make_muoi_den(path):
    """Tinh thể muối đen, lạnh, đe dọa."""
    img = Image.new("RGBA", (400, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    crystal = (40, 40, 60)
    glow = (100, 80, 140)
    white_glow = (200, 180, 240)
    # Các tinh thể
    for pts, col in [
        ([(200, 50), (260, 180), (200, 280), (140, 180)], (50, 45, 70)),
        ([(200, 80), (240, 180), (200, 250), (160, 180)], crystal),
        ([(120, 200), (200, 300), (150, 380), (80, 300)], (45, 40, 65)),
        ([(280, 200), (200, 300), (250, 380), (320, 300)], (45, 40, 65)),
        ([(200, 300), (260, 420), (200, 520), (140, 420)], crystal),
    ]:
        draw.polygon(pts, fill=col, outline=glow, width=2)
    # Mắt phát sáng
    for ex, ey in [(175, 200), (225, 200)]:
        oval(draw, ex, ey, 20, 18, (150, 100, 200))
        oval(draw, ex, ey, 12, 11, (220, 180, 255))
        oval(draw, ex, ey, 5, 5, (255, 255, 255))
    # Aura xung quanh
    for r in range(30, 5, -8):
        draw.ellipse([200 - r * 3, 50 - r, 200 + r * 3, 540 + r],
                     outline=(*glow, max(0, 80 - r * 3)), width=2)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img.save(path)
    print(f"  Char: {path}")


def make_cay_mit_me(path):
    """Cây mít mẹ to lớn, hiền từ."""
    img = Image.new("RGBA", (600, 900), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    trunk = (100, 70, 40)
    bark = (70, 45, 20)
    leaf = (60, 150, 50)
    dark_leaf = (40, 110, 35)
    fruit = (180, 140, 50)
    # Thân cây
    draw.rounded_rectangle([230, 400, 370, 900], radius=40, fill=trunk, outline=bark, width=5)
    for y in range(420, 880, 60):
        draw.line([(240, y), (360, y + 30)], fill=bark, width=3)
    # Tán lá (nhiều layer)
    for lx, ly, lrx, lry, col in [
        (300, 180, 220, 160, leaf), (180, 250, 160, 120, dark_leaf),
        (420, 250, 160, 120, dark_leaf), (300, 300, 250, 180, leaf),
        (170, 350, 130, 100, dark_leaf), (430, 350, 130, 100, dark_leaf),
        (300, 380, 200, 130, leaf),
    ]:
        oval(draw, lx, ly, lrx, lry, col, (30, 90, 25), 3)
    # Quả mít
    for fx, fy in [(220, 420), (350, 430), (260, 480)]:
        oval(draw, fx, fy, 40, 55, fruit, (130, 100, 30), 3)
        for gx in range(fx - 30, fx + 35, 10):
            draw.ellipse([gx, fy - 45, gx + 6, fy - 38], fill=(130, 100, 30))
    # Mặt cây mẹ (hiền từ)
    oval(draw, 300, 500, 55, 50, (140, 100, 55), bark, 3)
    draw.arc([260, 475, 295, 500], start=0, end=200, fill=bark, width=4)
    draw.arc([305, 475, 340, 500], start=0, end=200, fill=bark, width=4)
    draw.arc([270, 505, 330, 525], start=10, end=170, fill=bark, width=4)
    # Rễ
    for rx, ry in [(260, 820), (300, 840), (340, 820)]:
        draw.line([(rx, ry), (rx - 50, 900)], fill=bark, width=8)
        draw.line([(rx, ry), (rx + 50, 900)], fill=bark, width=6)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img.save(path)
    print(f"  Char: {path}")


if __name__ == "__main__":
    print("Tạo assets Hiệp Sĩ Hạt Mít...")

    # Backgrounds
    make_bg("assets/backgrounds/lang_ven_bien.jpg", "LÀNG VEN BIỂN",
            [(30, 90, 130), (20, 60, 100), (10, 40, 80)])
    make_bg("assets/backgrounds/rung_dua.jpg", "RỪNG DỪA NGHIÊNG",
            [(50, 120, 50), (30, 90, 30), (20, 60, 20)])
    make_bg("assets/backgrounds/nui_vo_gai.jpg", "NÚI VỎ GAI",
            [(80, 50, 30), (55, 35, 15), (40, 25, 10)])
    make_bg("assets/backgrounds/dam_man.jpg", "ĐẦM MẶN",
            [(20, 80, 100), (10, 55, 75), (5, 35, 55)])
    make_bg("assets/backgrounds/hang_kien.jpg", "HANG KIẾN ĐỎ",
            [(90, 30, 20), (65, 20, 10), (40, 10, 5)])
    make_bg("assets/backgrounds/dinh_nui.jpg", "ĐỈNH NÚI VỎ GAI",
            [(60, 40, 80), (40, 25, 60), (25, 15, 45)])
    make_bg("assets/backgrounds/bien_kho.jpg", "BIỂN KHÔ",
            [(100, 80, 50), (75, 60, 35), (50, 40, 20)])

    # Characters
    make_mit_coi("assets/characters/mit_coi.png")
    make_cua_kep_cat("assets/characters/cua_kep_cat.png")
    make_thay_vo_san("assets/characters/thay_vo_san.png")
    make_muoi_den("assets/characters/muoi_den.png")
    make_cay_mit_me("assets/characters/cay_mit_me.png")

    print("\nDone! Tất cả assets đã sẵn sàng.")
