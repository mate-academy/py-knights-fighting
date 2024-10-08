from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(**data).calculate_stats()
        for name, data in knights_config.items()
    }
    knights["lancelot"].take_damage(knights["mordred"])
    knights["mordred"].take_damage(knights["lancelot"])
    knights["arthur"].take_damage(knights["red_knight"])
    knights["red_knight"].take_damage(knights["arthur"])

    return {
        knight.name: knight.hp for knight in knights.values()
    }
