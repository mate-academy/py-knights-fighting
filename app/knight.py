from typing import List, Dict, Optional


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, int]],
        weapon: Dict[str, int],
        potion: Optional[Dict[str, Dict[str, int]]],
    ) -> None:
        self.name: str = name
        self.base_power: int = power
        self.hp: int = hp
        self.armour: List[Dict[str, int]] = armour
        self.weapon: Dict[str, int] = weapon
        self.potion: Optional[Dict[str, Dict[str, int]]] = potion
        self.protection: int = 0
        self.power: int = power

    def prepare_for_battle(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        if damage > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0
