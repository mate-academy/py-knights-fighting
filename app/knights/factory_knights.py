from app.equip_for_warriors.armour import Armour
from app.equip_for_warriors.potion import Potion
from app.equip_for_warriors.weapon import Weapon
from app.knights.warrior import Warrior
from app.knights.knight import Knight


def factory_knights(knights: dict) -> dict:

    knights_ = {}

    for name in knights.keys():
        warrior = Warrior(knights[name]["name"], knights[name]["hp"],
                          knights[name]["power"])

        list_armour = [Armour(armour["part"], armour["protection"])
                       for armour in knights[name]["armour"]]

        weapon = Weapon(knights[name]["weapon"]["name"],
                        knights[name]["weapon"]["power"])

        potion = None
        if knights[name]["potion"] is not None:
            potion = Potion(knights[name]["potion"]["name"],
                            knights[name]["potion"]["effect"])

        knight = Knight(warrior, list_armour, weapon, potion)
        knights_[knight.name] = knight

    return knights_
