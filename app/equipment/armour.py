from __future__ import annotations


class ArmourPart:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection


class TotalArmour:
    def __init__(self, armour_parts: list[ArmourPart]) -> None:
        self.armour = armour_parts

    def __iter__(self) -> TotalArmour:
        self.index = -1
        return self

    def __next__(self) -> ArmourPart:
        self.index += 1
        if self.index < len(self.armour):
            return self.armour[self.index]

        raise StopIteration
