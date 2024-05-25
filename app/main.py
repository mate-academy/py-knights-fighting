from app.knight_properties.knight import Knight
from app.knight_properties.weapon import Weapon

from app.dict_to_property.dict_to_armour import dict_to_armour
from app.dict_to_property.dict_to_potion import dict_to_potion
from app.other_funcs.battle import battle_func
from app.other_funcs.result_of_battle import result_of_battle


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, value in knights_config.items():
        name = value["name"]
        power = value["power"]
        hp = value["hp"]
        armour = dict_to_armour(value)
        weapon = Weapon(value["weapon"]["name"], value["weapon"]["power"])
        potion = dict_to_potion(value)
        knight = Knight(name, power, hp, armour, weapon, potion)
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()
        knights[key] = knight

    knights = battle_func(knights)

    return result_of_battle(knights)
