from __future__ import annotations
from typing import Union


class Armour:

    def __init__(self, protection_armour: int = 0) -> None:
        self.protection_armour = protection_armour

    def __add__(self, other: Union[int, Armour]) -> int:
        if isinstance(other, int):
            self.protection_armour += other
        else:
            self.protection_armour += other.protection_armour

        return self
