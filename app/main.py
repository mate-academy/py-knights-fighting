from app.knights_config import KNIGHTS
from app.realisation import (
    knight_battle_preparations,
    update_health_after_battle
)


def battle(knights: dict) -> dict:

    for knight in knights:
        knight_battle_preparations(knights[knight])

    update_health_after_battle(knights["lancelot"], knights["mordred"])
    update_health_after_battle(knights["arthur"], knights["red_knight"])

    return {
        knights[knight]["name"]: knights[knight]["hp"] for knight in knights
    }


print(battle(KNIGHTS))
