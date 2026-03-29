from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour] = None,
            weapon: dict = None,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.potion = potion
        self.armour = armour

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "hp" in effect:
                self.hp += effect["hp"]

    def calculate_total_protection(self) -> int:
        total_protection = sum(armour.protection for armour in self.armour)

        if self.potion is not None and "effect" in self.potion \
                and "protection" in self.potion["effect"]:
            total_protection += self.potion["effect"]["protection"]

        return total_protection


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection
