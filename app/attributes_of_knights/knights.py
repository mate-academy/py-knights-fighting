from app.attributes_of_knights.weapon import Weapon
from app.attributes_of_knights.armour import Armour
from app.attributes_of_knights.potion import Potion


class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, armour: list,
                 weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(a["part"],
                              a["protection"]) for a in armour]
        self.weapon = Weapon(weapon["name"],
                             weapon["power"]) if weapon else None
        self.potion = Potion(potion["name"],
                             potion["effect"]) if potion else None

    def calculate_protection(self) -> int:
        protection = sum(armour.protection for armour in self.armour)
        if self.potion and self.potion.effect.get("protection"):
            protection += self.potion.effect.get("protection")
        return protection

    def calculate_power(self) -> int:
        power = self.power + self.weapon.power \
            if self.weapon.power else self.power
        if self.potion and self.potion.effect.get("power"):
            power += self.potion.effect.get("power")
        return power

    def calculate_hp(self) -> int:
        hp = self.hp
        if self.potion and self.potion.effect.get("hp"):
            hp += self.potion.effect.get("hp")
        return hp
