from app.knights import Knight
from app.battles import battle_one


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(**characteristics)
        for name, characteristics in knights_config.items()
    }
    for instance_knight in knights.values():
        instance_knight.prepare_knight()
    battle_one(knights["lancelot"], knights["mordred"])
    battle_one(knights["arthur"], knights["red_knight"])
    return {knight.name: knight.hp for knight in knights.values()}
