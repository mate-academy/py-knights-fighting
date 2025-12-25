from typing import List, Dict, Optional


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: List[Dict[str, int]],
                 weapon: Dict[str, int],
                 potion: Optional[Dict[str, Dict[str, int]]] = None) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = sum(a["protection"] for a in armour)
        self.power = power + weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            self.hp += self.potion.get("effect", {}).get("hp", 0)
            self.power += self.potion.get("effect", {}).get("power", 0)
            self.protection += (
                self.potion.get("effect", {}).get("protection", 0))

    def take_damage(self, damage: int) -> None:
        net_damage = max(0, damage - self.protection)
        self.hp -= net_damage
        if self.hp < 0:
            self.hp = 0
