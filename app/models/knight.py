from typing import Dict, List, Optional

from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion


class Knight:
    name: str
    base_power: int
    hp: int
    weapon: Weapon
    armour: List[Armour]
    potion: Optional[Potion]
    power: int
    protection: int

    def __init__(self, config: Dict) -> None:
        self.name = config["name"]
        self.base_power = config["power"]
        self.hp = config["hp"]

        self.weapon = Weapon(**config["weapon"])
        self.armour = [Armour(**a) for a in config["armour"]]

        self.potion = Potion(**config["potion"]) if config["potion"] else None

        self.power = 0
        self.protection = 0

        self.prepare()

    def prepare(self) -> None:
        self.power = self.base_power + self.weapon.power
        self.protection = sum(a.protection for a in self.armour)

        if self.potion:
            self.apply_potion()

    def apply_potion(self) -> None:
        effects: Dict[str, int] = self.potion.effect if self.potion else {}

        self.power += effects.get("power", 0)
        self.hp += effects.get("hp", 0)
        self.protection += effects.get("protection", 0)

    def take_damage(self, enemy_power: int) -> None:
        damage: int = max(enemy_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)
