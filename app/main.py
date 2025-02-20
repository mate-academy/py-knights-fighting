from app.preparations.knights_stat import KNIGHTS
from app.preparations.make_knight import Knight
from app.battle.fight import fight


def battle(knights: dict) -> dict:

    prepared = []

    for knight, stats in knights.items():
        prepared.append(Knight(stats["name"],
                               stats["power"],
                               stats["hp"],
                               stats["armour"],
                               stats["weapon"],
                               stats["potion"]))

    first_fight = fight(prepared[0], prepared[2])
    second_fight = fight(prepared[1], prepared[3])

    return {
        prepared[0].name: first_fight[0],
        prepared[2].name: first_fight[1],
        prepared[1].name: second_fight[0],
        prepared[3].name: second_fight[1]
    }


print(battle(KNIGHTS))
