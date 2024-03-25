from app.knight.knight import Knight


def two_knights_battle(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection


def battle(knights: dict) -> dict:
    knights_dict = {knight: Knight(**knights[knight]) for knight in knights}

    two_knights_battle(knights_dict["lancelot"], knights_dict["mordred"])
    two_knights_battle(knights_dict["arthur"], knights_dict["red_knight"])

    return {
        knight.name: knight.hp if knight.hp >= 0 else 0
        for knight in knights_dict.values()
    }
