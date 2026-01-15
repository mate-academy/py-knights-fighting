from app.ammunition.armour import Armour
from app.ammunition.potion import Potion
from app.ammunition.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list = None,
                 weapon: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp

        self.armour = [Armour(**a) for a in armour] if armour else []
        self.weapon = Weapon(**weapon) if weapon else None
        self.potion = Potion(**potion) if potion else None

        self.power = self.base_power + self.weapon.power \
            if self.weapon else self.base_power
        self.hp = self.base_hp
        self.protection = self.calculate_protection()

        if self.potion:
            self.hp, self.power, self.protection = (
                self.potion.apply_effect(self.hp, self.power, self.protection))

    def calculate_protection(self) -> int:
        return sum(a.protection for a in self.armour)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
