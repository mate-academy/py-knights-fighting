from typing import Dict, List, Optional


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: List[Dict], weapon: Dict,
                 potion: Optional[Dict] = None) -> None:
        self.name: str = name
        self.base_power: int = power
        self.hp: int = hp
        self.armour: List[Dict] = armour
        self.weapon: Dict = weapon
        self.potion: Optional[Dict] = potion
        self.power: int = self.base_power
        self.protection: int = 0
        self.prepare_stats()

    def prepare_stats(self) -> None:
        self.power = self.base_power + self.weapon["power"]
        self.protection = sum(item["protection"] for item in self.armour)

        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    def protect_sum(self) -> int:
        return self.protection

    def hp_sum(self) -> int:
        return self.hp

    def power_sum(self) -> int:
        return self.power

    def take_damage(self, enemy_power: int) -> None:
        damage: int = max(0, enemy_power - self.protect_sum())
        self.hp = max(0, self.hp - damage)
