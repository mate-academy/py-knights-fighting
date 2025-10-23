from app.knights.equipment.weapon import Weapon
from app.knights.equipment.potion import Potion

class Knights:
    knights_dict = {}
    def __init__(self,
                 name: str,
                 name_knight: str,
                 power:  int,
                 hp: int,
                 armour: list,
                 weapon: Weapon,
                 potion: Potion
                 ):
        self.name = name
        self.name_knight = name_knight
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.knights_dict.update({self.name:
                                      {
                                          "name": self.name_knight,
                                          "power": self.power_total(),
                                          "hp": self.hp_total(),
                                          "armour":self.armour,
                                          "weapon":self.weapon,
                                          "potion":self.potion,
                                          "protection":self.protection_total()
                                      }})

    def hp_total(self):
        if not self.potion.hp is None:
            hp = self.hp + self.potion.hp
        else:
            hp = self.hp
        return hp

    def power_total(self):
        if not self.potion.power is None:
            power = self.power + self.potion.power + self.weapon.power
        else:
            power = self.power + self.weapon.power
        return power

    def protection_total(self):
        protection = 0
        if not self.potion.protection is None:
            protection = self.potion.protection

        if len(self.armour) > 0:
            for knight_armour in self.armour:
                protection += knight_armour.protection
        return protection