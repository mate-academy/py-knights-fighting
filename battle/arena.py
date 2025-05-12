from models.knight import Knight


def fight(knights: list[Knight]) -> None:
    name_to_knight = {k.name.lower(): k for k in knights}

    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red knight"),
    ]

    for name1, name2 in pairs:
        k1 = name_to_knight.get(name1)
        k2 = name_to_knight.get(name2)

        if not k1 or not k2:
            continue

        damage_k1 = max(k1.power - k2.protection, 0)
        damage_k2 = max(k2.power - k1.protection, 0)

        k2.hp -= damage_k1
        k1.hp -= damage_k2
