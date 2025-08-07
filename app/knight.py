from typing import List, Optional

from app.equipment import ArmourPart, Potion, Weapon


class Knight:
    def __init__(
        self,
        name: str,
        base_hp: int,
        base_power: int,
        armour: List[ArmourPart],
        weapon: Weapon,
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power
        self.armour_parts = armour
        self.weapon = weapon
        self.potion = potion

        self.hp = self._calculate_hp()
        self.power = self._calculate_power()
        self.protection = self._calculate_protection()

    def _calculate_protection(self) -> int:
        total = sum(part.protection for part in self.armour_parts)
        if self.potion:
            total += self.potion.protection
        return total

    def _calculate_power(self) -> int:
        total = self.base_power + self.weapon.power
        if self.potion:
            total += self.potion.power
        return total

    def _calculate_hp(self) -> int:
        total = self.base_hp
        if self.potion:
            total += self.potion.hp
        return total

    def take_damage(self, attack_power: int) -> None:
        damage = max(attack_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)

    def __repr__(self) -> str:
        return (
            f"{self.name}(HP={self.hp}, "
            f"Power={self.power}, Protection={self.protection})"
        )
