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
        if self.potion is None:
            return

        effect = self.potion.get("effect", {})
        for attribute, value in effect.items():
            current_value = getattr(self, attribute, None)
            if current_value is not None:
                setattr(self, attribute, current_value + value)
