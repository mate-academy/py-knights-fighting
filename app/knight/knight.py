from typing import Optional
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
            armour: Optional[list[dict]] = None,
            potion: Optional[Potion] = None

    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.protection = protection
        self.armour = armour if armour is not None else []
        self.potion = potion if potion is not None else None
