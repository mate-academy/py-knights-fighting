from app.stats.weapon import Weapon
from app.stats.armour import Armour
from app.stats.potion import Potion


class Knight:

    def __init__(self, name, power, hp, protection=0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

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

    def get_potion(self, knight_dict):
        if knight_dict["potion"] is not None:
            potion_dict = knight_dict["potion"]["effect"]
            if "hp" in potion_dict:
                potion_hp = potion_dict["hp"]
            else:
                potion_hp = 0
            if "power" in potion_dict:
                potion_power = potion_dict["power"]
            else:
                potion_power = 0
            if "protection" in potion_dict:
                potion_protection = potion_dict["protection"]
            else:
                potion_protection = 0
            knight_potion = Potion(knight_dict["potion"]["name"],
                                   potion_hp,
                                   potion_power,
                                   potion_protection)
            self.apply_potion(knight_potion)

    def fight(self, other):
        other_strength = other.power - self.protection
        self_strength = self.power - other.protection
        self.hp -= other_strength
        other.hp -= self_strength
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
