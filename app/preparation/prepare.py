from app.models.knight import Knight


def preparation(knights_config: dict) -> dict:
    prepared_knights = {}
    for name, data in knights_config.items():
        warrior = Knight(data)
        warrior.calculate_protection()
        warrior.add_power()
        warrior.add_potion()
        prepared_knights[name] = warrior

    return prepared_knights
