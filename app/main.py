from app.knights_data import KNIGHTS
from app.models import Knight
from app.battle_engine import duel


def battle(knights_config: dict) -> dict:
    fighters = {
        key: Knight(knight)
        for key, knight in knights_config.items()
    }

    duel(fighters["lancelot"], fighters["mordred"])
    duel(fighters["arthur"], fighters["red_knight"])

    return {
        fighter.name: fighter.hp
        for fighter in fighters.values()
    }


print(battle(KNIGHTS))
