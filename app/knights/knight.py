from __future__ import annotations

from app.items.consumables.potion import Potion
from app.items.equipment.armor.armour import Armour
from app.items.equipment.weapon.weapon import Weapon


class Knight:
    def __init__(
        self,
        data : dict,
    ) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.armour = [Armour(item) for item in data["armour"]]
        self.weapon = Weapon(data["weapon"])
        self.potion = Potion(data["potion"])
