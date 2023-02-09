from __future__ import annotations


class ArmourPart:

    def __init__(self,
                 name: str,
                 protection_level: int) -> None:
        self.name = name
        self.protection_level = protection_level


class SetArmourScope:

    def __init__(self, armour_parts: list[ArmourPart]) -> None:
        self.armour_parts = armour_parts
        self.protection_level = 0

    def calc_protection_level(self) -> int:
        if self.armour_parts:
            return sum([armour.protection_level
                        for armour in self.armour_parts])
        return 0

    def show_armour_scope(self) -> list | str:
        if self.armour_parts:
            return [armour.name for armour in self.armour_parts]
        return "The knight has no armour"


class Weapon:

    def __init__(self,
                 name: str,
                 power: int) -> None:
        self.name = name
        self.power = power


class Potion:

    def __init__(self,
                 name: str,
                 effect: dict) -> None:
        self.name = name
        self.effect = effect
