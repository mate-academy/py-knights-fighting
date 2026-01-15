from app.config.knight import Knight
from app.config.stats import KNIGHTS

MATCHUPS = [("lancelot", "mordred"), ("arthur", "red Knight")]


def create_knights(knights_stats: dict) -> dict:
    return {name: Knight(**stats) for name, stats in knights_stats.items()}


def battle(knights_stats: dict) -> dict:
    knights = create_knights(knights_stats)
    for knight in knights.values():
        knight.battle_preparation()

    for name1, name2 in MATCHUPS:
        knight1 = knights.get(name1)
        knight2 = knights.get(name2)

        knight1.take_damage(knight2.power)
        knight2.take_damage(knight1.power)

    return {knight.name: knight.hp for knight in knights.values()}

knights = create_knights(KNIGHTS)
for knight in knights.values():
    knight.battle_preparation()
    print(knight)

# print(create_knights(KNIGHTS))
