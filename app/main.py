from app.characters.knights import KNIGHTS
from app.characters.knight import Knight

from app.characters.lancelot import lancelot
from app.characters.arthur import arthur
from app.characters.mordred import mordred
from app.characters.red_knight import red_knight

from app.characters.list_of_knight import list_of_knight


def battle(knights_config) -> dict:
    # BATTLE PREPARATIONS:
    knights_list = []

    for key, value in knights_config.items():
        knight = Knight(
            name=key,
            power=value["power"],
            hp=value["hp"],
            armour=value["armour"],
            weapon=value["weapon"],
            potion=value["potion"]
        )
        knight.get_ready()
        knights_list.append(knight)
    print(knights_list[0].power)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    list_of_knight[0].hp -= list_of_knight[2].power - list_of_knight[0].protection
    list_of_knight[2].hp -= list_of_knight[0].power - list_of_knight[2].protection

    # check if someone fell in battle
    if list_of_knight[0].hp <= 0:
        list_of_knight[0].hp = 0

    if list_of_knight[2].hp <= 0:
        list_of_knight[2].hp = 0

    # 2 Arthur vs Red Knight:
    list_of_knight[1].hp -= list_of_knight[3].power - list_of_knight[1].protection
    list_of_knight[3].hp -= list_of_knight[1].power - list_of_knight[3].protection

    # check if someone fell in battle
    if list_of_knight[1].hp <= 0:
        list_of_knight[1].hp = 0

    if list_of_knight[3].hp <= 0:
        list_of_knight[3].hp = 0

    # Return battle results:
    return {
        list_of_knight[0].name: list_of_knight[0].hp,
        list_of_knight[1].name: list_of_knight[1].hp,
        list_of_knight[2].name: list_of_knight[2].hp,
        list_of_knight[3].name: list_of_knight[3].hp,
    }


print(battle(KNIGHTS))
