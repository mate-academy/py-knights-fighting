from typing import Dict, List, Optional


class Knight:
    def __init__(self, config: Dict) -> None:
        self.name: str = config["name"]
        self.base_power: int = config["power"]
        self.hp: int = config["hp"]
        self.armour: List[Dict] = config["armour"]
        self.weapon: Dict = config["weapon"]
        self.potion: Optional[Dict] = config["potion"]

        self.power: int = self.base_power
        self.protection: int = 0

    def apply_armour(self) -> None:
        self.protection = sum(
            part["protection"] for part in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if not self.potion:
            return

        effects = self.potion["effect"]

        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)
        self.hp += effects.get("hp", 0)

    def prepare(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
