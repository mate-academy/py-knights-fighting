from app.knights import KNIGHTS
from app.battle import knight_battle_preparations, after_battle


def battle(knights: dict) -> dict:

    for knight in knights:
        knight_battle_preparations(knights[knight])

    after_battle(knights["lancelot"], knights["mordred"])
    after_battle(knights["arthur"], knights["red_knight"])

    return {
        knights[knight]["name"]: knights[knight]["hp"] for knight in knights
    }


print(battle(KNIGHTS))
