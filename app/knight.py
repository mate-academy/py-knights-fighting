# knight.py
class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self):
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion:
            self.hp += self.potion["effect"]["hp"]
            self.power += self.potion["effect"]["power"]

    def prepare_for_battle(self):
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
