from app.items.weapon import Weapon
from app.items.armour import Armour
from app.items.potion import Potion


class Inventory:
    def __init__(self,
                 weapon: dict = None,
                 armours: list[dict] = [],
                 potion: dict = None
                 ) -> None:
        self.weapon = self.weapon_add(weapon)
        self.armours = self.armours_add(armours)
        self.potion = self.potion_add(potion)

    @staticmethod
    def weapon_add(weapon):
        if weapon:
            return Weapon(weapon["name"], weapon["power"])
        else:
            return None

    @staticmethod
    def armours_add(armours):
        if armours:
            return [
                Armour(arm["part"], arm["protection"]) for arm in armours]
        else:
            return []

    @staticmethod
    def potion_add(potion):
        if potion:
            return Potion(potion["name"], potion["effect"])
        else:
            return None
