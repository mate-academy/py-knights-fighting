from app.warriors.knights import Knights


def battle(knights_config: dict) -> dict:
    knights = [Knights(**data) for data in knights_config.values()]

    for i in range(len(knights) // 2):
        k1 = knights[i]
        k2 = knights[i + len(knights) // 2]

        k1.hp -= k2.power - k1.protection
        k2.hp -= k1.power - k2.protection

        k1.hp = max(k1.hp, 0)
        k2.hp = max(k2.hp, 0)

    return {k.name: k.hp for k in knights}
