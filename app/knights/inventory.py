from app.items.weapon import Weapon
from app.items.armour import Armour
from app.items.potion import Potion


class Inventory:
    def __init__(self, weapon: dict, armours: list[dict], potion: dict) -> None:
        if weapon:
            self.weapon = Weapon(weapon["name"], weapon["power"])
        else:
            self.weapon = None

        if armours:
            self.armour = [Armour(arm["part"], arm["protection"]) for arm in armours]
        else:
            self.armour = []

        if potion:
            self.potion = Potion(potion["name"], potion["effect"])
        else:
            self.potion = None
