from app.items.armor import Armor
from app.items.sword import Sword
from app.items.potion import Potion


class Inventory:
    def __init__(self,
                 i_weapon=None,
                 i_armors=None,
                 i_potion=None
                 ) -> None:
        if i_weapon:
            self.weapon = Sword(i_weapon["name"], i_weapon["power"])
        else:
            self.weapon = None

        if i_armors:
            self.armors = [
                Armor(arm["part"], arm["protection"])
                for arm in i_armors
            ]
        else:
            self.armors = []

        if i_potion:
            self.potion = Potion(i_potion["name"], i_potion["effect"])
        else:
            self.potion = None
