from app.knight_class import Knight
from app.knights_config import KNIGHTS


def battle_preparation(knight: Knight) -> None:
    """Function prepare knight for a battle"""
    knight.get_armour()
    knight.get_weapon()
    knight.get_potion()


def duel(knight_1: Knight, knight_2: Knight) -> None:
    """
    Function simulate a duel between two knights
    and changes knight`s health_points by results
    """
    knight_1.hp += (knight_1.protection - knight_2.power)
    knight_2.hp += (knight_2.protection - knight_1.power)


def check_if_fell(knight: Knight) -> None:
    """Function checks if knight fell"""
    if knight.hp <= 0:
        knight.hp = 0


def battle_results(knights: dict) -> dict:
    """Function returns a dictionary with results of a knights battle"""
    return {knight.name: knight.hp for knight in knights}


def battle(knights: dict) -> dict:
    """Function simulate the course of the battle"""
    knights_instance_dict = {name: Knight(name, knights) for name in knights}

    for knight in knights_instance_dict.values():
        battle_preparation(knight)

    duel(knights_instance_dict["lancelot"], knights_instance_dict["mordred"])
    duel(knights_instance_dict["arthur"], knights_instance_dict["red_knight"])

    for knight in knights_instance_dict.values():
        check_if_fell(knight)

    return battle_results(knights_instance_dict.values())


print(battle(KNIGHTS))
