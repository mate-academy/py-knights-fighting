
from app.config import get_knights
from app.battle import Battle

knights = get_knights()
def battle(knights):
    battles = [
        ("Lancelot", "Mordred"),
        ("Arthur", "Red Knight"),
    ]

    results = []

    for name1, name2 in battles:
        k1 = knights[name1]
        k2 = knights[name2]
        b = Battle(k1, k2)
        result = b.fight()
        results.append(result)

    return results


print(battle(knights))