from typing import List, Dict, Optional


class Knight:
    def __init__(self,
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
        self.apply_potion()

    @property
    def power(self) -> int:
        return self.base_power \
            + self.weapon["power"] \
            + self.potion_effect.get("power", 0)

    @property
    def hp(self) -> int:
        return self.base_hp + self.potion_effect.get("hp", 0)

    @property
    def protection(self) -> int:
        base_protection = sum(part["protection"] for part in self.armour)
        return base_protection + self.potion_effect.get("protection", 0)

    def apply_potion(self) -> None:
        self.potion_effect = self.potion["effect"] if self.potion else {}

    def __repr__(self) -> str:
        return f"{self.name} " \
               f"(HP: {self.hp}, " \
               f"Power: {self.power}, " \
               f"Protection: {self.protection})"
