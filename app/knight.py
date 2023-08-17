from typing import List, Dict, Any


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Dict[str, int]],
            weapon: Dict[str, Any],
            potion: Dict[str, Any]
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = 0
        self.calculate_stats()

    def calculate_stats(self) -> None:
        self.protection = sum(
            part["protection"] for part in self.armour
        )
        self.power = self.base_power + self.weapon["power"]
        if self.potion:
            self.apply_potion_effects()

    def apply_potion_effects(self) -> None:
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]
        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]
        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]
