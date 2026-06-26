from __future__ import annotations

from dataclasses import dataclass

from app.character.armour import Armour
from app.character.potion import Potion
from app.character.weapon import Weapon


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Potion | None = None
    protection = 0

    def increase_protection(self) -> Knight:
        for armour in self.armour:
            self.protection += armour.protection

        return self

    def increase_power(self) -> Knight:
        self.power += self.weapon.power

        return self

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        effect_keys = list(self.potion.effect.__dict__.keys())

        for key in effect_keys:
            try:
                current_value = getattr(self, key)
                setattr(
                    self,
                    key,
                    current_value + self.potion.effect.get_effect_value(key)
                )
            except AttributeError:
                print(f"AttributeError: {key} does not exist.")

    def __isub__(self, other: Knight) -> Knight:
        self.hp -= other.power - self.protection

        if self.hp <= 0:
            self.hp = 0

        return self
