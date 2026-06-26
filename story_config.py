"""
Story configuration for YouTube Shorts.
Each 'scene' defines: background, characters, dialogue, duration, effects.
"""

STORY = {
    "title": "Câu chuyện: Chú Mèo Lười & Deadline",
    "language": "vi",  # 'vi' for Vietnamese, 'en' for English
    "output_name": "shorts_cat_deadline",
    "scenes": [
        {
            "id": 1,
            "background": "assets/backgrounds/office.jpg",
            "characters": [
                {"image": "assets/characters/cat.png", "position": "center", "scale": 0.6}
            ],
            "text": "Khi deadline còn 5 phút...",
            "narration": "Khi deadline còn 5 phút...",
            "duration": 3.0,
            "effect": "zoom_in",
            "text_position": "top",
        },
        {
            "id": 2,
            "background": "assets/backgrounds/office.jpg",
            "characters": [
                {"image": "assets/characters/cat.png", "position": "left", "scale": 0.5}
            ],
            "text": "Mèo: Bình tĩnh nào... 😎",
            "narration": "Mèo nói: Bình tĩnh nào",
            "duration": 3.5,
            "effect": "shake",
            "text_position": "bottom",
        },
        {
            "id": 3,
            "background": "assets/backgrounds/chaos.jpg",
            "characters": [
                {"image": "assets/characters/cat.png", "position": "center", "scale": 0.7}
            ],
            "text": "30 giây sau...",
            "narration": "30 giây sau...",
            "duration": 2.0,
            "effect": "flash",
            "text_position": "center",
        },
        {
            "id": 4,
            "background": "assets/backgrounds/chaos.jpg",
            "characters": [
                {"image": "assets/characters/cat.png", "position": "right", "scale": 0.8}
            ],
            "text": "Mèo: ĐỪNG HOẢNG LOẠN!!!\n(đang hoảng loạn)",
            "narration": "Mèo hét: Đừng hoảng loạn. Nhưng đang hoảng loạn thật sự.",
            "duration": 4.0,
            "effect": "zoom_out",
            "text_position": "bottom",
        },
        {
            "id": 5,
            "background": "assets/backgrounds/office.jpg",
            "characters": [],
            "text": "Cuối cùng... nộp đúng giờ! 🎉\n(bằng cách copy của bạn)",
            "narration": "Cuối cùng nộp đúng giờ! Bằng cách copy của bạn.",
            "duration": 4.0,
            "effect": "fade_in",
            "text_position": "center",
        },
    ],
    "outro": {
        "text": "Follow để xem thêm! 👍",
        "duration": 2.5,
    }
}
