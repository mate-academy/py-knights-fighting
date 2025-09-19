from typing import Dict, List, Optional


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: List[Dict],
                 weapon: Dict,
                 potion: Optional[Dict] = None) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.armour: List[Dict] = armour
        self.weapon: Dict = weapon
        self.potion: Optional[Dict] = potion
        self.apply_effects()

    def apply_effects(self) -> None:
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)

    def protect_sum(self) -> int:
        sum_protection: int = 0
        for item in self.armour:
            sum_protection += item["protection"]
        if (self.potion and "effect"
                in self.potion and "protection"
                in self.potion["effect"]):
            sum_protection += self.potion["effect"]["protection"]
        return sum_protection

    def hp_sum(self) -> int:
        return self.hp

    def power_sum(self) -> int:
        attack: int = self.power
        attack += self.weapon["power"]
        return attack

    def take_damage(self, enemy_power: int) -> None:
        damage: int = max(0, enemy_power - self.protect_sum())
        self.hp = max(0, self.hp - damage)
