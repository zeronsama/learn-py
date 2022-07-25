def get_second_elem(List: list):
    return List[1]


TVshow = [
    ("Gu,hotm", 1.4),
    ("Tpdoth", 1.343),
    ("Mfwdm", 0.92),
    ("NCsbil", 0.862),
    ("It", 0.553),
    ("S", 0.411),
    ("EodA", 0.164),
    ("Tpsotnft", 0.259),
    ("Dd", 0.394),
    ("Ml", 0.562),
]
TVshow.sort(key=get_second_elem, reverse=True)
print("电视剧的收视率排行榜：")
for tuple in TVshow:
    print(f"《{tuple[0]}》  收视率：{tuple[1]}%")
