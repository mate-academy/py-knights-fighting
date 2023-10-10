from __future__ import annotations

from typing import List


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: dict,
        armour: list = None,
        potion: dict = None,
        protection: int = 0,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = protection
        self.update_total_protection()
        self.update_power_from_weapon()
        self.update_power_and_hp_from_potion()

    def update_total_protection(self) -> None:
        base_protection = self.protection

        armour_protection = sum(
            part_armour.get("protection", 0)
            for part_armour in self.armour
            if self.armour
        )

        potion_protection = (
            self.potion.get("effect", {}).get("protection", 0)
            if self.potion else 0
        )

        self.protection = (base_protection + armour_protection
                           + potion_protection)

    def update_power_from_weapon(self) -> None:
        power_weapon = self.weapon.get("power", 0) if self.weapon else 0
        self.power += power_weapon

    def update_power_and_hp_from_potion(self) -> None:
        power_potion = (
            self.potion.get("effect", {}).get("power", 0)
            if self.potion is not None
            else 0
        )
        hp_potion = (
            self.potion.get("effect", {}).get("hp", 0)
            if self.potion is not None else 0
        )

        self.power += power_potion
        self.hp += hp_potion

    def attack(self, other_knight: Knight) -> None:
        self.hp -= max(other_knight.power - self.protection, 0)
        other_knight.hp -= max(self.power - other_knight.protection, 0)

        self.hp = max(self.hp, 0)
        other_knight.hp = max(other_knight.hp, 0)

    def __repr__(self) -> str:
        return (
            f"{self.name}, power={self.power}, hp={self.hp}, "
            f"protection={self.protection}"
        )


class Battle:
    def __init__(self, knights: List[Knight]) -> None:
        self.knights = knights

    def fight(self) -> None:
        self.knights[0].attack(self.knights[2])
        self.knights[1].attack(self.knights[3])

    def results_battle(self) -> dict:
        return {knight.name: knight.hp for knight in self.knights}
