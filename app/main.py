from app.knight_properties.knight import Knight
from app.knight_properties.weapon import Weapon

from app.dict_to_property.dict_to_armour import dict_to_armour
from app.dict_to_property.dict_to_potion import dict_to_potion


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

    knights_list = list(knights.keys())

    for i in range(len(knights_list) // 2):
        knights[knights_list[i]].battle(knights[knights_list[i + 2]])
        knights[knights_list[i + 2]].battle(knights[knights_list[i]])

    return {value.name: value.hp for value in knights.values()}
