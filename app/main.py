from typing import Dict

from app.knights import Knight
from app.knight_config import knights_config


def conduct_battle(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)


def battle(knights: any) -> Dict[str, int]:
    for knight_name, knight in knights_config.items():
        knight.apply_effects()

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for knight1_name, knight2_name in battles:
        conduct_battle(
            knights_config[knight1_name],
            knights_config[knight2_name]
        )

    return {knight.name: knight.hp for knight in knights_config.values()}
