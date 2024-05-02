from app.players.knight import Knight
from app.battles.duel import duel


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(**knight)
        for name, knight in knights_config.items()
    }
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
