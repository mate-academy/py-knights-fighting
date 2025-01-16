from app.initializate.knight import Knight
from app.stats.Head import Main
from app.stats.armour import Armour
from app.stats.potion import Potion
from app.stats.weapon import Weapon


def init_input(knights: dict) ->\
        dict[str, list[Main | Armour | Potion | Weapon]]:
    object_knights = {}
    for data in knights.values():
        main = Main(data["name"], data["power"], data["hp"])
        armour = Armour(data["armour"])
        weapon = Weapon(data["weapon"])
        potion = Potion(data["potion"])
        object_knights[data["name"]] = [main, armour, weapon, potion]
    return object_knights


def make_knight_object(objects_knights: dict) -> list[Knight]:
    test_list = []
    for value in objects_knights.values():
        test_list.append(Knight(*value))
    return test_list
