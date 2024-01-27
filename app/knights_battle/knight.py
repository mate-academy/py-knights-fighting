from app.knights_battle.equipment import Armour, Weapon, Potion

class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(a["part"], a["protection"]) for a in armour] if armour else []
        self.weapon = None
        self.potion = None
        self.protection = 0

        # If weapon is provided, create a Weapon object
        if weapon:
            self.weapon = Weapon(weapon["name"], weapon["power"])

        # If potion is provided, create a Potion object
        if potion:
            self.potion = Potion(potion["name"], potion["effect"])

    def apply_armour(self):
        for a in self.armour:
            self.protection += a.protection

    def apply_weapon(self):
        if self.weapon:
            self.power += self.weapon.power

    def apply_potion(self):
        if self.potion:
            for attr, effect in self.potion.effect.items():
                setattr(self, attr, getattr(self, attr) + effect)

