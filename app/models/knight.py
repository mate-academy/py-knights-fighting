from typing import List, Dict, Optional


class Knight:
    def __init__(
            self, name: str,
            power: int,
            hp: int,
            armour: List[Dict[str, int]],
            weapon: Dict[str, any],
            potion: Optional[Dict[str, Dict[str, int]]] = None
    ) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.armour: List[Dict[str, int]] = armour
        self.weapon: Dict[str, any] = weapon
        self.potion: Optional[Dict[str, Dict[str, int]]] = potion

    def apply_potion(self) -> None:
        if self.potion:
            for stat, effect in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + effect)

    def total_protection(self) -> int:
        return sum(item["protection"] for item in self.armour)

    def prepare_for_battle(self) -> None:
        self.apply_potion()
        self.power += self.weapon["power"]
        self.protection: int = self.total_protection()
