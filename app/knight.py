from app.accessories import Armour, Weapon, Potion


class Knight:
    knights = dict()

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        Knight.knights[name] = self

    def apply_armour(self, armour: Armour) -> None:
        self.armour = armour
        self.protection += armour.total_protection()

    def apply_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        self.potion = potion
        self.protection += potion.protection
        self.power += potion.power
        self.hp += potion.hp

    def apply_everything(
            self,
            armours: Armour,
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.apply_armour(armours)
        self.apply_weapon(weapon)
        self.apply_potion(potion)


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0
