from typing import Optional, List, Dict


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
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = sum(
            armour_piece["protection"]
            for armour_piece in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effects = self.potion["effect"]
            for effect_name, effect_value in effects.items():
                current_value = getattr(self, effect_name, 0)
                setattr(self, effect_name, current_value + effect_value)
