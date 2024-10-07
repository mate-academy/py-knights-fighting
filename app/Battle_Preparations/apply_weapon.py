def apply_weapon(knights_attr:dict) -> None:
    for knight, stats in knights_attr.items():
        stats.power += stats.weapon["power"]

