from typing import Optional, List, Dict, Union


class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: List[Dict[str, Union[str, int]]],
                 weapon: Dict[str, Union[str, int]],
                 potion: Optional[Dict[str, Union[str, Dict[str, int]]]]
                 = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()

    def apply_armor(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            for stat, value in effect.items():
                attribute_name = stat
                current_value = getattr(self, attribute_name, 0)
                setattr(self, attribute_name, current_value + value)
