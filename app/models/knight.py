from typing import List, Optional

from app.models.armour import Armour
from app.models.potion import Potion
from app.models.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour],
            weapon: Weapon,
            potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def calculate_stats(self) -> dict[str, int]:
        total_hp = self.hp
        total_power = self.power + self.weapon.power

        total_protection = 0
        for armour in self.armour:
            total_protection += armour.protection

        if self.potion is not None:
            for stat, effect_value in self.potion.effect.items():
                if stat == "hp":
                    total_hp += effect_value
                elif stat == "power":
                    total_power += effect_value
                elif stat == "protection":
                    total_protection += effect_value

        return {
            "total_hp": total_hp,
            "total_power": total_power,
            "total_protection": total_protection,
        }
