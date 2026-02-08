from app.battle import Battle
from app.charcters.knightinfo import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight.from_dict(config)
        for name, config in knights_config.items()
    }
    for knight in knights.values():
        knight.prepare_for_battle()

    Battle.fight(knights["lancelot"], knights["mordred"])
    Battle.fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
