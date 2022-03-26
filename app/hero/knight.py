from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


class Knights():

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: Weapon, potion: Potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.use_armour()
        if potion:
            self.use_potion()
        self.use_weapon()

    @staticmethod
    def create_knight(KNIGHT_dict):
        weapon = Weapon.create_weapons(KNIGHT_dict["weapon"])
        potion = Potion.create_potion(KNIGHT_dict["potion"])
        armour = [Armour.create_armour(item) for item in KNIGHT_dict["armour"]]

        knight = Knights(name=KNIGHT_dict["name"],
                         power=KNIGHT_dict["power"],
                         hp=KNIGHT_dict["hp"],
                         armour=armour,
                         weapon=weapon,
                         potion=potion)
        return knight

    def use_armour(self):
        self.protection += sum(
            armour_obj.protection
            for armour_obj in self.armour
        )

    def use_potion(self):
        self.power += self.potion.power
        self.hp += self.potion.hp
        self.protection += self.potion.protection

    def use_weapon(self):
        self.power += self.weapon.power

    def fight(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
