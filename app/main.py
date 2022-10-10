# for pytest
from .knights.configurations import KNIGHTS
from .knights.armour import Armour
from .knights.knight import Knight
from .knights.potion import Potion
from .knights.weapon import Weapon

# for pycharm
# from knights.configurations import KNIGHTS
# from knights.armour import Armour
# from knights.knight import Knight
# from knights.potion import Potion
# from knights.weapon import Weapon


def battle_preparations(knights_config: tuple) -> dict:
    """
    The function creates a list of knights from the configuration dictionary
    for the battle
    """
    knights = {}
    for knight_name, knight_info in knights_config.items():
        new_knight = Knight(
            knight_info["name"], knight_info["hp"], knight_info["power"]
        )

        for armour_info in knight_info["armour"]:
            new_armour = Armour.create_armour(armour_info)
            if new_armour is not None:
                new_knight.set_armour(new_armour)

        new_weapon = Weapon.create_weapon(knight_info["weapon"])
        if new_weapon is not None:
            new_knight.set_weapon(new_weapon)

        new_potion = Potion.create_potion(knight_info["potion"])
        if new_potion is not None:
            new_knight.set_potion(new_potion)

        knights[knight_name] = new_knight
    return knights


def battle_first(knights: dict) -> dict:
    """
    The function conducts one round of battle
    """
    battle_list = ["lancelot", "arthur", "mordred", "red_knight"]
    battle_pair = [(0, 2), (1, 3)]

    for pair in battle_pair:
        knights[battle_list[pair[0]]].fights(knights[battle_list[pair[1]]])

    return {knights[knight].name: knights[knight].get_hp()
            for knight in battle_list}


def battle(knights_config: dict) -> tuple:
    """
    The function conducts battle
    """
    knights_dict = battle_preparations(knights_config)
    battle_result = battle_first(knights_dict)
    return battle_result


print(battle(KNIGHTS))
