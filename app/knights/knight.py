from typing import Optional, List
from app.knights.potion import Potion
from app.knights.weapon import Weapon
from app.knights.armour import Armour


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: Optional[List[Armour]] = None,
                 weapon: Optional[Weapon] = None,
                 potion: Optional[Potion] = None,
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        if armour:
            self.protection += sum(a.protection for a in armour)

        if weapon:
            self.power += weapon.power

        if potion:
            potion.apply(self)

    def take_damage(self, damage: int) -> None:
        self.hp = max(self.hp - damage, 0)
