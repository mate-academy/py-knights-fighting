from app.fighter.weapon_definition import Weapon
from app.fighter.armour_definition import Armour
from app.fighter.potion_definition import Potion


class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def count_ability(self, weapon, potion_tuple, armour_protection):
        potion_power, potion_hp, potion_protection = potion_tuple
        self.power += weapon.power + potion_power
        self.hp += potion_hp
        self.protection += potion_protection + armour_protection

    def prepare_knight(self):
        knight_armour = Armour()
        knight_weapon = Weapon(self.weapon["name"], self.weapon["power"])
        if self.potion is not None:
            knight_potion = Potion(self.potion["name"], self.potion["effect"])
            self.count_ability(knight_weapon, knight_potion.count_effect(),
                               knight_armour.count_protection(self.armour))
        else:
            self.count_ability(knight_weapon, (0, 0, 0),
                               knight_armour.count_protection(self.armour))
