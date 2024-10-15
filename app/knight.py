from typing import Dict, Any
from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.armour = Armour(
            data["armour"]
        ) if "armour" in data else Armour([])
        self.weapon = Weapon(
            data["weapon"]["name"],
            data["weapon"]["power"]
        )
        self.potion = Potion(
            data["potion"]["name"],
            data["potion"]["effect"]
        ) if data["potion"] else None
        self.apply_potion()
        self.calculate_stats()

    def apply_potion(self) -> None:
        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.armour.protection += self.potion.effect.get("protection", 0)

    def calculate_stats(self) -> None:
        self.power += self.weapon.power
