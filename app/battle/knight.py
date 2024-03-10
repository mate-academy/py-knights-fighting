from weapon import Weapon
from potion import Potion

class Knight:
    def __init__(self, name, power, hp, weapon=None, potion=None):
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.potion = potion

    def apply_potion(self):
        if self.potion:
            self.hp += self.potion.hp_effect
            self.power += self.potion.power_effect

    def battle(self, opponent):
        # Battle logic here