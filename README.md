# 🌱 Hiệp Sĩ Hạt Mít — YouTube Shorts Generator

Series hoạt hình short tự động tạo video từ cốt truyện, nhân vật và background.

## Render video trên GitHub (dùng điện thoại)

1. Vào tab **Actions** trên GitHub
2. Chọn **"🎬 Render Episode"**
3. Bấm **"Run workflow"**
4. Chọn mùa + tập → bấm **Run**
5. Chờ ~5 phút → tải file MP4 về

## Chạy local (máy tính)

```bash
pip install -r requirements.txt
python generate_hatmit_assets.py      # tạo assets lần đầu
python render_episode.py --season 1 --episode 1
```

## Chạy web app

```bash
python app.py
# Mở http://localhost:5000 trên điện thoại (cùng wifi)
```

## Cấu trúc

| File | Mô tả |
|------|-------|
| `series_hatmit.py` | Config toàn bộ 80 tập (4 mùa) |
| `create_short.py` | Engine render: ghép ảnh, hiệu ứng, TTS, xuất MP4 |
| `render_episode.py` | CLI render từng tập |
| `app.py` | Web app mobile-friendly |
| `generate_hatmit_assets.py` | Tạo assets nhân vật + background |
