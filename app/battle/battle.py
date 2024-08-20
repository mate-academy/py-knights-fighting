from __future__ import annotations

from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.heroes.knight import Knight
from app.potion.potion import Potion


def battle(knights: dict) -> dict:
    knight_list = config_knights((knights))

    fight(knight_list[0], knight_list[2])
    fight(knight_list[1], knight_list[3])

    result = {}
    for knight in knight_list:
        result.update({knight.name: knight.hp})
    return result


def fight(knight_1: Knight, knight_2: Knight) -> dict:
    knight_1.hp = knight_1.get_hp() - (knight_2.get_power()
                                       - knight_1.get_protection())
    knight_2.hp = knight_2.get_hp() - (knight_1.get_power()
                                       - knight_2.get_protection())

    knight_1.hp = check_health(knight_1.hp)
    knight_2.hp = check_health(knight_2.hp)

    return {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp
    }


def check_health(health: int) -> int:
    if health <= 0:
        health = 0
    return health


def config_knights(knights: dict) -> list[Knight]:
    knight_list = []
    for knight in knights.values():
        knight_list.append(
            Knight(knight["name"], knight["power"], knight["hp"],
                   [Armour(arm["part"], arm["protection"]) for arm
                    in knight["armour"]],
                   Weapon(knight["weapon"]["name"], knight["weapon"]["power"]),
                   Potion(knight["potion"]["name"], knight["potion"]["effect"])
                   if knight["potion"] is not None else None)
        )
    return knight_list
