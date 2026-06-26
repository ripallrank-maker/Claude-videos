"""
Hiệp Sĩ Hạt Mít — Series Config
80 tập, 4 mùa. Mỗi entry là một tập short (35-60 giây).
"""

SERIES_META = {
    "title": "HIỆP SĨ HẠT MÍT",
    "subtitle": "Đường Lên Núi Bái Sư",
    "language": "vi",
    "style": "folk_fantasy",
    "output_dir": "output/hatmit",
    "fps": 30,
}

# ---------------------------------------------------------------------------
# Nhân vật & assets
# ---------------------------------------------------------------------------
CHARS = {
    "mit_coi":    "assets/characters/mit_coi.png",
    "cua":        "assets/characters/cua_kep_cat.png",
    "thay":       "assets/characters/thay_vo_san.png",
    "muoi_den":   "assets/characters/muoi_den.png",
    "cay_me":     "assets/characters/cay_mit_me.png",
}

BG = {
    "lang":   "assets/backgrounds/lang_ven_bien.jpg",
    "rung":   "assets/backgrounds/rung_dua.jpg",
    "nui":    "assets/backgrounds/nui_vo_gai.jpg",
    "dam":    "assets/backgrounds/dam_man.jpg",
    "hang":   "assets/backgrounds/hang_kien.jpg",
    "dinh":   "assets/backgrounds/dinh_nui.jpg",
    "bien":   "assets/backgrounds/bien_kho.jpg",
}


def char(name, pos="center", scale=0.55):
    return {"image": CHARS[name], "position": pos, "scale": scale}


# ---------------------------------------------------------------------------
# MÙA 1 — Rời biển lên núi bái sư (Tập 1–20)
# ---------------------------------------------------------------------------
MUA_1 = [
    # ---- Tập 1 ----
    {
        "episode": 1,
        "season": 1,
        "title": "Hạt Mít Bị Chê",
        "youtube_title": "Hạt mít bé xíu đòi làm hiệp sĩ 😤 | Hiệp Sĩ Hạt Mít Tập 1",
        "output_name": "s1e01_hat_mit_bi_che",
        "scenes": [
            {
                "id": 1,
                "background": BG["lang"],
                "characters": [char("mit_coi", "center", 0.55)],
                "text": "Một hạt mít bé xíu tuyên bố\nmình sẽ trở thành HIỆP SĨ!",
                "narration": "Một hạt mít bé xíu tuyên bố mình sẽ trở thành hiệp sĩ!",
                "duration": 3.5,
                "effect": "zoom_in",
                "text_position": "top",
            },
            {
                "id": 2,
                "background": BG["lang"],
                "characters": [
                    char("mit_coi", "center", 0.55),
                    char("cay_me", "right", 0.65),
                ],
                "text": "Mít Cối: Ta sẽ bảo vệ cả làng!\n(Dân làng cười ồ)",
                "narration": "Mít Cối hô to: Ta sẽ bảo vệ cả làng! Dân làng cười ồ vì cậu quá nhỏ và tròn.",
                "duration": 5.0,
                "effect": "shake",
                "text_position": "bottom",
            },
            {
                "id": 3,
                "background": BG["lang"],
                "characters": [char("mit_coi", "left", 0.45)],
                "text": "Cậu biểu diễn vài đường kiếm...\nrồi tự xoay vòng té nhào 😵",
                "narration": "Cậu cố biểu diễn vài đường kiếm, nhưng tự xoay vòng rồi đâm đầu vào vỏ dừa.",
                "duration": 4.5,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 4,
                "background": BG["lang"],
                "characters": [
                    char("mit_coi", "left", 0.45),
                    char("cay_me", "right", 0.70),
                ],
                "text": 'Cây Mít Mẹ:\n"Bên trong mỗi hạt giống\nđều có một cái mầm đang ngủ..."',
                "narration": "Cây Mít Mẹ dịu dàng nói: Bên trong mỗi hạt giống đều có một cái mầm đang ngủ.",
                "duration": 5.0,
                "effect": "fade_in",
                "text_position": "bottom",
            },
            {
                "id": 5,
                "background": BG["lang"],
                "characters": [],
                "text": "Ngoài khơi... ⚠️\nmột đám mây đen mang hạt MUỐI đang tiến vào!",
                "narration": "Nhưng ngoài khơi, một đám mây đen mang theo những hạt muối lấp lánh đang tiến vào làng...",
                "duration": 4.0,
                "effect": "flash",
                "text_position": "center",
            },
        ],
        "outro": {"text": "Tập 2: Cơn Bão Muối Đen ⚡\nĐể xem tiếp, nhấn Follow! 🌱", "duration": 3.0},
    },

    # ---- Tập 2 ----
    {
        "episode": 2,
        "season": 1,
        "title": "Cơn Bão Muối Đen",
        "youtube_title": "Cây mít mẹ bị hóa đá!! 😱 | Hiệp Sĩ Hạt Mít Tập 2",
        "output_name": "s1e02_bao_muoi_den",
        "scenes": [
            {
                "id": 1,
                "background": BG["lang"],
                "characters": [],
                "text": "Chỉ sau một đêm...\nlá cây trong làng bắt đầu KHÔ LẠI!",
                "narration": "Chỉ sau một đêm, lá cây trong làng bắt đầu khô lại.",
                "duration": 3.0,
                "effect": "zoom_in",
                "text_position": "top",
            },
            {
                "id": 2,
                "background": BG["lang"],
                "characters": [char("mit_coi", "left", 0.5), char("muoi_den", "right", 0.6)],
                "text": "Muối Đen xuất hiện!\nMít Cối lao ra chống lại cơn bão...",
                "narration": "Muối Đen xuất hiện dưới dạng bóng tinh thể giữa mây. Mít Cối lao ra chống lại nhưng bị thổi bay vì quá nhẹ.",
                "duration": 5.5,
                "effect": "shake",
                "text_position": "bottom",
            },
            {
                "id": 3,
                "background": BG["lang"],
                "characters": [
                    char("cay_me", "center", 0.75),
                    char("mit_coi", "left", 0.4),
                ],
                "text": "Cây Mít Mẹ dùng rễ chắn bão\nbảo vệ dân làng...",
                "narration": "Cây Mít Mẹ dùng rễ chắn bão cho dân làng. Muối Đen cười rằng vùng đất này sắp khô cạn.",
                "duration": 5.0,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 4,
                "background": BG["lang"],
                "characters": [char("cay_me", "center", 0.75)],
                "text": "Cây Mẹ bị hóa đá một nửa...\nvà thả xuống một chiếc gai phát sáng!",
                "narration": "Cây Mít Mẹ bị hóa đá một nửa và thả xuống một chiếc gai mít phát sáng cho Mít Cối.",
                "duration": 5.0,
                "effect": "flash",
                "text_position": "bottom",
            },
            {
                "id": 5,
                "background": BG["lang"],
                "characters": [char("mit_coi", "center", 0.55)],
                "text": "⚡ Chiếc gai chỉ thẳng về\nngọn núi xa xôi...",
                "narration": "Chiếc gai phát sáng chỉ thẳng về một ngọn núi xa xôi...",
                "duration": 4.0,
                "effect": "zoom_out",
                "text_position": "center",
            },
        ],
        "outro": {"text": "Tập 3: Lời Tiên Tri Trên Vỏ Mít\nFollow để xem tiếp! 🌱", "duration": 3.0},
    },

    # ---- Tập 3 ----
    {
        "episode": 3,
        "season": 1,
        "title": "Lời Tiên Tri Trên Vỏ Mít",
        "youtube_title": "Hạt mít đọc lời tiên tri cổ! 📜 | Hiệp Sĩ Hạt Mít Tập 3",
        "output_name": "s1e03_loi_tien_tri",
        "scenes": [
            {
                "id": 1,
                "background": BG["lang"],
                "characters": [char("mit_coi", "center", 0.55)],
                "text": "Chiếc gai phát sáng...\nchỉ về NÚI VỎ GAI!",
                "narration": "Chiếc gai phát sáng chỉ về Núi Vỏ Gai.",
                "duration": 3.0,
                "effect": "zoom_in",
                "text_position": "top",
            },
            {
                "id": 2,
                "background": BG["lang"],
                "characters": [char("mit_coi", "left", 0.5), char("cay_me", "right", 0.65)],
                "text": '"Hạt cuối cùng muốn cứu cây,\nphải lên Núi Vỏ Gai bái sư."',
                "narration": "Dân làng tìm thấy dòng chữ cổ trên vỏ mít mẹ: Hạt cuối cùng muốn cứu cây, phải lên Núi Vỏ Gai bái sư.",
                "duration": 5.5,
                "effect": "fade_in",
                "text_position": "bottom",
            },
            {
                "id": 3,
                "background": BG["lang"],
                "characters": [char("mit_coi", "center", 0.5)],
                "text": "Mít Cối xung phong đi!\nDân làng: ổng chưa từng rời bãi biển...",
                "narration": "Mít Cối xung phong đi ngay, nhưng dân làng lo cậu chưa từng rời khỏi bãi biển.",
                "duration": 4.5,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 4,
                "background": BG["lang"],
                "characters": [char("mit_coi", "center", 0.55)],
                "text": "Mít Cối run sợ...\nnhưng vẫn ôm chiếc gai vào lòng 💪",
                "narration": "Mít Cối run sợ nhưng vẫn ôm chiếc gai vào lòng.",
                "duration": 4.0,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 5,
                "background": BG["lang"],
                "characters": [char("mit_coi", "left", 0.5), char("cua", "right", 0.5)],
                "text": "Khi vừa bước ra khỏi làng...\nCUA KẸP CÁT chặn đường! 🦀",
                "narration": "Khi cậu vừa bước ra khỏi làng, Cua Kẹp Cát chặn đường và giơ càng lên thách đấu.",
                "duration": 4.0,
                "effect": "flash",
                "text_position": "center",
            },
        ],
        "outro": {"text": "Tập 4: Trận Đấu Với Cua Kẹp Cát 🦀\nFollow để không bỏ lỡ! 🌱", "duration": 3.0},
    },

    # ---- Tập 4 ----
    {
        "episode": 4,
        "season": 1,
        "title": "Trận Đấu Với Cua Kẹp Cát",
        "youtube_title": "Hạt mít đấu với cua khổng lồ! 🦀 | Hiệp Sĩ Hạt Mít Tập 4",
        "output_name": "s1e04_dau_voi_cua",
        "scenes": [
            {
                "id": 1,
                "background": BG["lang"],
                "characters": [char("mit_coi", "left", 0.5), char("cua", "right", 0.65)],
                "text": "Mít Cối phải đánh bại\ncua to GẤP BA lần mình!",
                "narration": "Mít Cối phải đánh bại một con cua to gấp ba lần mình để rời khỏi bãi biển.",
                "duration": 3.5,
                "effect": "zoom_in",
                "text_position": "top",
            },
            {
                "id": 2,
                "background": BG["lang"],
                "characters": [char("mit_coi", "center", 0.5), char("cua", "right", 0.65)],
                "text": "Cua kẹp vào áo choàng,\nquay vòng rồi ném xuống cát!",
                "narration": "Cua Kẹp Cát kẹp vào áo choàng Mít Cối, quay vòng rồi ném xuống cát.",
                "duration": 5.0,
                "effect": "shake",
                "text_position": "bottom",
            },
            {
                "id": 3,
                "background": BG["lang"],
                "characters": [char("mit_coi", "center", 0.5)],
                "text": "Mít Cối nhận ra:\nthân tròn có thể LĂN rất nhanh! 💡",
                "narration": "Trong lúc bị rượt, Mít Cối nhận ra thân mình tròn có thể lăn rất nhanh.",
                "duration": 4.5,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 4,
                "background": BG["lang"],
                "characters": [char("mit_coi", "left", 0.45), char("cua", "right", 0.6)],
                "text": "Lăn vòng quanh Cua...\nCua chóng mặt, tự kẹp hai càng! 😂",
                "narration": "Cậu lăn vòng quanh Cua khiến Cua chóng mặt và tự kẹp hai càng vào nhau.",
                "duration": 5.0,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 5,
                "background": BG["lang"],
                "characters": [char("cua", "right", 0.6)],
                "text": 'Cua chịu thua:\n"Đường lên núi còn có thứ\nKẸP ĐAU hơn cả càng cua..." ⚠️',
                "narration": "Cua chịu thua nhưng bảo rằng đường lên núi còn có thứ kẹp đau hơn cả càng cua.",
                "duration": 4.0,
                "effect": "zoom_out",
                "text_position": "bottom",
            },
        ],
        "outro": {"text": "Tập 5: Bạn Đồng Hành Đi Ngang 🦀\nFollow để xem tiếp! 🌱", "duration": 3.0},
    },

    # ---- Tập 5 ----
    {
        "episode": 5,
        "season": 1,
        "title": "Bạn Đồng Hành Đi Ngang",
        "youtube_title": "Kẻ vừa đánh nhau lại đòi đi theo! 🦀 | Hiệp Sĩ Hạt Mít Tập 5",
        "output_name": "s1e05_ban_dong_hanh",
        "scenes": [
            {
                "id": 1,
                "background": BG["lang"],
                "characters": [char("cua", "right", 0.6), char("mit_coi", "left", 0.5)],
                "text": "Kẻ vừa đánh nhau với Mít Cối\nlại đòi đi theo cậu!",
                "narration": "Kẻ vừa đánh nhau với Mít Cối lại đòi đi theo cậu.",
                "duration": 3.5,
                "effect": "zoom_in",
                "text_position": "top",
            },
            {
                "id": 2,
                "background": BG["lang"],
                "characters": [char("cua", "right", 0.6), char("mit_coi", "left", 0.5)],
                "text": 'Cua: "Tao đi để giám sát\nthằng hạt tròn này khỏi chết lãng xẹt!"',
                "narration": "Cua thấy Mít Cối không bỏ cuộc nên quyết định đi cùng để giám sát thằng hạt tròn này khỏi chết lãng xẹt.",
                "duration": 5.0,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 3,
                "background": BG["rung"],
                "characters": [char("cua", "right", 0.55), char("mit_coi", "left", 0.5)],
                "text": "Vấn đề: Cua chỉ biết đi NGANG...\nCả hai cứ lệch hướng mãi 😅",
                "narration": "Vấn đề là Cua chỉ biết đi ngang, khiến cả hai liên tục lệch khỏi đường.",
                "duration": 4.5,
                "effect": "shake",
                "text_position": "bottom",
            },
            {
                "id": 4,
                "background": BG["rung"],
                "characters": [char("mit_coi", "center", 0.5)],
                "text": "Mít Cối dùng chiếc gai phát sáng\nlàm la bàn! 🧭",
                "narration": "Họ cãi nhau về hướng đi. Cuối cùng, Mít Cối dùng chiếc gai phát sáng làm la bàn.",
                "duration": 4.0,
                "effect": "none",
                "text_position": "bottom",
            },
            {
                "id": 5,
                "background": BG["dam"],
                "characters": [],
                "text": "Chiếc gai chỉ về ĐẦM MẶN...\nBiển cảnh: \"Không hạt giống nào trở về\" ⚠️",
                "narration": "Chiếc gai chỉ về phía Đầm Mặn, nơi có biển cảnh báo: Không hạt giống nào trở về.",
                "duration": 4.0,
                "effect": "flash",
                "text_position": "center",
            },
        ],
        "outro": {"text": "Tập 6: Chiếc Thuyền Lá Chuối 🚢\nFollow để không bỏ lỡ! 🌱", "duration": 3.0},
    },
]

# ---------------------------------------------------------------------------
# (Mùa 2, 3, 4 sẽ được thêm vào theo cùng cấu trúc)
# ---------------------------------------------------------------------------
MUA_2 = []  # TODO: Tập 21–40
MUA_3 = []  # TODO: Tập 41–60
MUA_4 = []  # TODO: Tập 61–80

ALL_EPISODES = MUA_1 + MUA_2 + MUA_3 + MUA_4


def get_episode(season: int, episode: int):
    for ep in ALL_EPISODES:
        if ep["season"] == season and ep["episode"] == episode:
            return ep
    return None
