from app.knights.knight import Knight
from app.battle import battle_preparation, duel


def battle(knights_config: dict) -> dict:
    knights_dict = {
        key: Knight(value) for key, value in knights_config.items()
    }
    battle_preparation(knights_dict)
    duel(knights_dict["lancelot"], knights_dict["mordred"])
    duel(knights_dict["arthur"], knights_dict["red_knight"])

    return {knight.name: knight.hp for knight in knights_dict.values()}
