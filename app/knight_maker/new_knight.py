from typing import Optional, List
from app.items.items_by_knight import Armour, Weapon, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Optional[Weapon] = None,
            armour: Optional[List[Armour]] = None,
            potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    def prepare_stats(self) -> dict:
        hp_final = self.hp
        power_final = self.power
        protection_final = 0
        if self.weapon is not None:
            power_final += self.weapon.power

        if self.armour:
            for part in self.armour:
                protection_final += part.protection

        if self.potion is not None:
            effect = getattr(self.potion, "effect", {}) or {}
            hp_final += effect.get("hp", 0)
            power_final += effect.get("power", 0)
            protection_final += effect.get("protection", 0)
        protection_final = max(0, protection_final)
        return ({"hp": hp_final,
                "power": power_final,
                 "protection": protection_final})
