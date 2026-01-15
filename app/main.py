from app.config.knight import Knight

MATCHUPS = [("lancelot", "mordred"), ("arthur", "red_knight")]


def create_knights(knights_stats: dict) -> dict:
    return {name: Knight(**stats) for name, stats in knights_stats.items()}


def battle(knights_stats: dict) -> dict:
    knights = create_knights(knights_stats)
    for knight in knights.values():
        knight.battle_preparation()

    for name1, name2 in MATCHUPS:
        knight1 = knights.get(name1)
        knight2 = knights.get(name2)

        if knight1 and knight2:
            dmg_to_knight1 = max(0, knight2.power - knight1.protection)
            dmg_to_knight2 = max(0, knight1.power - knight2.protection)

            knight1.hp = max(0, knight1.hp - dmg_to_knight1)
            knight2.hp = max(0, knight2.hp - dmg_to_knight2)

    return {knight.name: knight.hp for knight in knights.values()}
