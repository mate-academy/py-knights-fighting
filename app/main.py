from app.models.knight import Knight  # Capital K
from app.engine.battle_arena import fight


def battle(knights_config: dict) -> dict:

    knights = {
        key: Knight(config) for key, config in knights_config.items()
    }

    # Execute the predefined battles
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
