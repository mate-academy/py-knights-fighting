from app.knight_properties.knight import Knight
from app.knight_properties.weapon import Weapon

from app.other_funcs.battle import battle_func
from app.other_funcs.result_of_battle import result_of_battle
from app.knight_properties.armour import dict_to_armour
from app.knight_properties.potion import dict_to_potion


def battle(knights_config: dict) -> dict:
    knights = {}
    for name, properties in knights_config.items():
        name = properties["name"]
        power = properties["power"]
        hp = properties["hp"]
        armour = dict_to_armour(properties)
        weapon = Weapon(properties["weapon"]["name"],
                        properties["weapon"]["power"])
        potion = dict_to_potion(properties)
        knight = Knight(name, power, hp, armour, weapon, potion)
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()
        knights[name] = knight

    knights = battle_func(knights)

    return result_of_battle(knights)
