from app.stats.weapon import Weapon
from app.stats.armour import Armour


class Knight:

    def __init__(self, name, power, hp, protection=0):
        self.name = name
        self.protection = protection
        self.power = power
        self.hp = hp
        self.potion = None

    def apply_armour(self, armour):
        self.protection += armour.protection

    def get_armour(self, knight_dict):
        knight_armour = knight_dict["armour"]
        if len(knight_armour) > 0:
            for piece in knight_armour:
                armour_piece = Armour(piece["part"], piece["protection"])
                self.apply_armour(armour_piece)

    def apply_weapon(self, weapon):
        self.power += weapon.power

    def get_weapon(self, knight_dict):
        knight_weapon_dict = knight_dict["weapon"]
        knight_weapon = Weapon(knight_weapon_dict["name"],
                               knight_weapon_dict["power"])
        self.apply_weapon(knight_weapon)

    def apply_potion(self, potion):
        self.power += potion.power
        self.hp += potion.hp
        self.protection += potion.protection

    def get_potion(self):
        stats = ("power", "hp", "protection")
        for stat in stats:
            setattr(self, stat, getattr(self, stat) + self.potion["effect"][stat])

    def fight(self, other):
        other_strength = other.power - self.protection
        self_strength = self.power - other.protection
        self.hp -= other_strength
        other.hp -= self_strength
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
