def apply_weapon(knights: dict) -> None:
    for knight, stats in knights.items():
        stats["power"] += stats["weapon"]["power"]
