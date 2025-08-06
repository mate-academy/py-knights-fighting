from app.battle_preparation.armour import Armour
from app.battle_preparation.knight import Knight
from app.battle_preparation.weapon import Weapon
from app.battle_preparation.potion import Potion


def creating_knights(dictionary: dict) -> dict[Knight]:
    result = {}
    for value in dictionary.values():
        obj = Knight(name=value["name"], power=value["power"], hp=value["hp"])
        result[value["name"]] = obj
    return result


def creating_armors(dictionary: dict) -> dict[list[Armour]]:
    result = {}
    for value in dictionary.values():
        list_of_armors = []
        if value["armour"] != []:
            for armour in value["armour"]:
                obj = Armour(part=armour["part"],
                             protection=armour["protection"])
                list_of_armors.append(obj)
        result[value["name"]] = list_of_armors
    return result


def creating_weapons(dictionary: dict) -> dict[Weapon]:
    result = {}
    for value in dictionary.values():
        obj = Weapon(name=value["weapon"]["name"],
                     power=value["weapon"]["power"])
        result[value["name"]] = obj
    return result


def creating_potions(dictionary: dict) -> dict[Potion]:
    result = {}
    for value in dictionary.values():
        if value["potion"] is not None:
            obj = Potion(name=value["potion"]["name"],
                         effect=value["potion"]["effect"])
            result[value["name"]] = obj
    return result
