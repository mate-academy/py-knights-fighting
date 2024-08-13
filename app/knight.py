from typing import List, Dict, Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Dict[str, int]],
            weapon: Dict[str, int],
            potion: Optional[Dict[str, Dict[str, int]]] = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        self.power = self.base_power + self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            self.hp = self.base_hp + effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
        else:
            self.hp = self.base_hp

    def __str__(self) -> str:
        return f"{self.name}: HP={self.hp}, " \
               f"Power={self.power}, Protection={self.protection}"
