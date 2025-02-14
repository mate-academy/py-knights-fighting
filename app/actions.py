from app.init_data import Knight


def init_knights(knights_config: dict) -> dict:
    return {name: Knight(**knight) for name, knight in knights_config.items()}


def attack(fighters: dict) -> dict:
    lancelot = fighters["lancelot"]
    arthur = fighters["arthur"]
    mordred = fighters["mordred"]
    red_knight = fighters["red_knight"]

    lancelot - mordred
    arthur - red_knight

    return {knight.name: knight.hp for knight in fighters.values()}
