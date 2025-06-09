from app.knights.classes import Armour, Potion, Weapon


class Knights:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armours: list[Armour],
                 weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours
        self.weapon = weapon
        self.potion = potion

    def sum_protection(self) -> int:
        rezult_protection = 0
        for armour in self.armours:
            rezult_protection += armour.protection
        if self.potion is not None:
            rezult_protection += self.potion.effect_protection
        return rezult_protection

    def sum_power(self) -> int:
        rezult_power = self.power + self.weapon.weapon_power
        if self.potion is not None:
            rezult_power += self.potion.effect_power
        return rezult_power

    def sum_hp(self) -> int:
        rezult_hp = self.hp
        if self.potion is not None:
            rezult_hp += self.potion.effect_hp
        return rezult_hp
