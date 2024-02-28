from __future__ import annotations
from typing import Any


class KnightsCharacteristics:

    def __init__(
        self,
        knight: dict[str, Any]
    ) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.weapon = knight["weapon"]
        self.armour = knight["armour"]
        self.potion = knight["potion"]

    def protection(self) -> int:
        protection = 0
        for armour_piece in self.armour:
            protection += armour_piece.get("protection")

        if self.potion:
            if "protection" in self.potion["effect"]:
                protection += self.potion["effect"]["protection"]

        return protection

    def total_power(self) -> int:

        t_power = self.power + self.weapon["power"]

        if self.potion:
            if "power" in self.potion["effect"]:
                t_power += self.potion["effect"]["power"]

        return t_power

    def total_hp(self) -> int:
        hp = self.hp

        if self.potion:
            if "hp" in self.potion["effect"]:
                hp += self.potion["effect"]["hp"]
        return hp
