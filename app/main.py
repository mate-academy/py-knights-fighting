from __future__ import annotations
from app.characters import Knight


def battle(knights: dict) -> dict:
    """
    This function takes dict of 4 knights
    with names("lancelot", "arthur", "moldred", "red_knight"),
    creates 4 objects of class Knight and plays a fight between them
    :param knights: dict of knights like:
    name: {name, power, hp, armour, weapon, potion}
    :return: dict of knights like name: hp
    """
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.create_from_dict(knights["lancelot"])

    # arthur
    arthur = Knight.create_from_dict(knights["arthur"])

    # mordred
    mordred = Knight.create_from_dict(knights["mordred"])

    # red_knight
    red_knight = Knight.create_from_dict(knights["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
