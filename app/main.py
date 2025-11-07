from typing import cast

from app.knight.knight import Knight, create_knight


def battle(knights: dict) -> dict:
    knight_names = list(knights.keys())
    knight_objects = {
        name: cast(Knight, create_knight(name, knights))
        for name in knight_names
    }

    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    results = {}
    for k1, k2 in pairs:
        knight_1 = knight_objects[k1]
        knight_2 = knight_objects[k2]
        results[knight_1.name] = knight_1.count_hp(knight_2)
        results[knight_2.name] = knight_2.count_hp(knight_1)

    return results
