from typing import Optional

from app.knight.armour import Armour
from app.knight.weapon import Weapon
from app.knight.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            protection: int = 0,
            armour: Optional[Armour] = None,
            potion: Optional[Potion] = None

    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour if armour else Armour()
        self.protection = self.armour.total_protection()
        self.potion = potion if potion is not None else None
