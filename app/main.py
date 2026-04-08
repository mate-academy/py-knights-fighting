from app.models.knight import Knight


def battle(knights_config: dict) -> dict[str, int]:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }

    Knight.fight(knights["lancelot"], knights["mordred"])

    Knight.fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
