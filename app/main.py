from app.models.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(value)
        for key, value in knights_config.items()
    }

    knights["lancelot"].attack(knights["mordred"])
    knights["mordred"].attack(knights["lancelot"])

    knights["arthur"].attack(knights["red_knight"])
    knights["red_knight"].attack(knights["arthur"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
