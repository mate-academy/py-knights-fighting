from __future__ import annotations
from app.util.armour import get_armor
from app.util.weapon import get_weapon


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = knight["power"] + get_weapon(knight)
        self.protection = get_armor(knight)
        self.get_potion(knight)

    def get_potion(self, knight: dict) -> None:
        if knight["potion"]:
            potion_effect = knight["potion"]["effect"]
            for effect in potion_effect:
                if effect == "power":
                    self.power += potion_effect[effect]
                if effect == "protection":
                    self.protection += potion_effect[effect]
                if effect == "hp":
                    self.hp += potion_effect[effect]
