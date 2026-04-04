from __future__ import annotations

from typing import List, Dict


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: None | List[Dict[str, str | int]],
            weapon: Dict[str, str | int],
            potion: None | Dict[str, str | Dict[str, int]]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def __str__(self) -> str:
        return self.name
