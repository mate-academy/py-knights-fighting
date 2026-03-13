from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }
    knights["lancelot"].take_damage(knights["mordred"].power)
    knights["mordred"].take_damage(knights["lancelot"].power)
    knights["arthur"].take_damage(knights["red_knight"].power)
    knights["red_knight"].take_damage(knights["arthur"].power)

    return {
        k.name: k.hp
        for k in knights.values()
    }
