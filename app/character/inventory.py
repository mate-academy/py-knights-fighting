from app.items.armor import Armor
from app.items.sword import Sword
from app.items.potion import Potion


class Inventory:
    def __init__(self,
                 weapon: dict = None,
                 armors: dict = None,
                 potion: dict = None) -> None:
        if weapon:
            self.weapon = Sword(weapon["name"], weapon["power"])
        else:
            self.weapon = None

        if armors:
            self.armors = [
                Armor(armour["part"], armour["protection"])
                for armour in armors
            ]
        else:
            self.armors = []

        if potion:
            self.potion = Potion(potion["name"], potion["effect"])
        else:
            self.potion = None
