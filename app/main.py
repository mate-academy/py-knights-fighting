from app.knight.warrior import Warrior
from app.knight.warrior import Knight
from app.armed.weapon import Weapon
from app.armed.armour import Armour
from app.armed.potion import Potion
from app.constant import KNIGHTS


def battle(knight_dict: dict) -> dict:

    warriors = dict()
    weapons = dict()
    armours = dict()
    knight_arms = dict()
    knights_potion = dict()
    for man, warrior in knight_dict.items():

        # call warriors, not knights
        warriors[man] = Warrior(
            name=warrior["name"],
            power=warrior["power"],
            hp=warrior["hp"]
        )

        # create weapons collection (as dict)
        weapons[man] = Weapon(
            name=warrior["weapon"]["name"],
            power=warrior["weapon"]["power"]
        )

        # create armours collection
        knight_arms[man] = list()
        for armour in warrior["armour"]:
            if f'{armour["part"]}_{armour["protection"]}' not in armours:
                armours[f'{armour["part"]}_{armour["protection"]}'] \
                    = Armour(armour["part"], armour["protection"])

            # make warriors knights-like
            # assign arms to warrior
            knight_arms[man].append(
                armours[f'{armour["part"]}_{armour["protection"]}']
            )

        # make warriors knights-like
        # assign potion
        if not warrior["potion"] is None:
            knights_potion[man] = Potion(
                name=warrior["potion"]["name"],
                effect=warrior["potion"]["effect"]
            )

    # print("\n ----------- warriors --------------------")
    # for man, warrior in warriors.items():
    #     print(f"{man} = {warrior.__dict__}")

    # make Knights out of the Warriors
    knight = dict()
    # print("\n ----------- KNIGHTS --------------------")
    for warrior in warriors:
        knight[warrior] = Knight(warriors[warrior])
        knight[warrior].weapon_on(weapons[warrior])
        knight[warrior].armour_on(knight_arms[warrior])
        if warrior in knights_potion:
            knight[warrior].potion_on(knights_potion[warrior])

        # print(f"{knight[warrior].warrior.name} = "
        #       f"power: {knight[warrior].power}, "
        #       f"hp: {knight[warrior].hp}, "
        #       f"protection: {knight[warrior].protection}"
        #       )

    # print("\n ----------- BATTLE result --------------------")
    # 1 Lancelot vs Mordred:
    knight["lancelot"] * knight["mordred"]
    # 2 Arthur vs Red Knight:
    knight["arthur"] * knight["red_knight"]

    # for warrior in warriors:
    #     print(f"{knight[warrior].warrior.name} = "
    #           f"power: {knight[warrior].power}, "
    #           f"hp: {knight[warrior].hp}, "
    #           f"protection: {knight[warrior].protection}"
    #           )

    return {_knight.warrior.name: _knight.hp for _knight in knight.values()}


print(battle(KNIGHTS))
