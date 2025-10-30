from typing import Optional
from app.knights.equipment import Weapon, ArmourPart, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            armour: list[ArmourPart],
            potion: Optional[Potion]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self._protection = self.calculate_protection()
        self.apply_potion()

    def calculate_protection(self) -> int:
        return sum(part.protection for part in self.armour)

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion.effect.items():
                if stat == "protection":
                    self._protection += value
                elif stat == "power":
                    self.power += value
                elif stat == "hp":
                    self.hp += value

    @property
    def effective_power(self) -> int:
        return self.power + self.weapon.power

    @property
    def protection(self) -> int:
        return self._protection

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage)
        if self.hp < 0:
            self.hp = 0
