from app.knights.knight import Knight


def preparing(knights_config: dict) -> dict:
    prepared_knights = {}
    for name, data in knights_config.items():
        warrior = Knight(data)
        warrior.use_protection()
        warrior.use_weapon()
        warrior.use_potion()
        prepared_knights[name] = warrior

    return prepared_knights
