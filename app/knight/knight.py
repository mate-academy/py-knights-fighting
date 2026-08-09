from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion | None = None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        if potion:
            self.potion = potion
        else:
            self.potion = None

    def calculate_power(self) -> int:
        power = self.power
        power += self.weapon.power
        if self.potion:
            power += self.potion.power
        return power

    def calculate_protection(self) -> int:
        protection = 0
        if self.armour:
            for armour in self.armour:
                protection += armour.protection

        if self.potion:
            protection += self.potion.protection
        return protection

    def calculate_hp(self) -> int:
        hp = self.hp
        if self.potion:
            hp += self.potion.hp
        return hp
