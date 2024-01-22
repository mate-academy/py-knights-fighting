from typing import List, Optional, Dict, Union


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, int]],
        weapon: Dict[str, int],
        potion: Optional[Dict[str, Union[int, Dict[str, int]]]]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection: Optional[int] = None

    def apply_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    # In Knight class
    def apply_potion(self, potion_effect: dict) -> None:
        if potion_effect:
            self.hp += potion_effect.get("hp", 0)
            self.power += potion_effect.get("power", 0)
            self.protection += potion_effect.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        if self.potion:
            self.apply_potion(self.potion["effect"])
