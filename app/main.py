from app.characters.knights import KNIGHTS
from app.characters.knight import Knight

from app.characters.lancelot import lancelot
from app.characters.arthur import arthur
from app.characters.mordred import mordred
from app.characters.red_knight import red_knight

from app.characters.list_of_knight import list_of_knight


def battle(knights_config) -> dict:
    # BATTLE PREPARATIONS:
    knights_list = {}

    for key, value in knights_config.items():
        knight = Knight(
            name=value,
            power=value["power"],
            hp=value["hp"],
            armour=value["armour"],
            weapon=value["weapon"],
            potion=value["potion"]
        )
        knight.get_ready()
        knights_list[f"{key}"] = knight
    for key, value in knights_list.items():
        print("Key: ", key)
        print(list_of_knight["lancelot"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    list_of_knight["lancelot"].hp -= list_of_knight["mordred"].power - list_of_knight["lancelot"].protection
    list_of_knight["mordred"].hp -= list_of_knight["lancelot"].power - list_of_knight["mordred"].protection

    # check if someone fell in battle
    if list_of_knight["lancelot"].hp <= 0:
        list_of_knight["lancelot"].hp = 0

    if list_of_knight["mordred"].hp <= 0:
        list_of_knight["mordred"].hp = 0

    # 2 Arthur vs Red Knight:
    list_of_knight["arthur"].hp -= red_knight.power - list_of_knight["arthur"].protection
    list_of_knight["red_knight"].hp -= list_of_knight["arthur"].power - list_of_knight["red_knight"].protection

    # check if someone fell in battle
    if list_of_knight["arthur"].hp <= 0:
        list_of_knight["arthur"].hp = 0

    if list_of_knight["red_knight"].hp <= 0:
        list_of_knight["red_knight"].hp = 0

    # Return battle results:
    return {
        list_of_knight["lancelot"].name: list_of_knight["lancelot"].hp,
        list_of_knight["arthur"].name: list_of_knight["arthur"].hp,
        list_of_knight["mordred"].name: list_of_knight["mordred"].hp,
        list_of_knight["red_knight"].name: list_of_knight["red_knight"].hp,
    }


print(battle(KNIGHTS))
