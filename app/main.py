from app.knights.Knights_config import KNIGHTS
from app.knights.knight import Knight


def battle_of_knights(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection


def battle(knights: dict) -> dict:
    knights_dict = {knight: Knight(**knights[knight]) for knight in knights}

    battle_of_knights(knights_dict["lancelot"], knights_dict["mordred"])
    battle_of_knights(knights_dict["arthur"], knights_dict["red_knight"])

    return {knight.name: knight.hp
            if knight.hp >= 0
            else 0
            for knight in knights_dict.values()}


print(battle(KNIGHTS))
