from typing import List, Dict, Optional


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: List[Dict[str, int]], weapon: Dict[str, int],
                 potion: Optional[Dict[str, Dict[str, int]]] = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage - self.protection)
        if self.hp < 0:
            self.hp = 0
