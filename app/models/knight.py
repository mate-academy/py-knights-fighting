from typing import Optional
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Optional[list[Armour]] = None,
        weapon: Optional[Weapon] = None,
        potion: Optional[Potion] = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.hp = hp
        self.power = power
        self.protection = 0

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour.protection

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def apply_potion(self) -> None:
        if not self.potion:
            return
        for stat, value in self.potion.effect.items():
            if stat == "hp":
                self.hp += value
            elif stat == "power":
                self.power += value
            elif stat == "protection":
                self.protection += value

    def take_hit(self, dmg: int) -> None:
        dmg_taken = max(dmg - self.protection, 0)
        self.hp = max(self.hp - dmg_taken, 0)
