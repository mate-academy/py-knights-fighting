
class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion=None):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self):
        total_protection = sum([piece.protection for piece in self.armour])
        return total_protection

    def apply_weapon(self):
        return self.power + self.weapon.power

    def apply_potion(self):
        if self.potion:
            effect = self.potion.get_effect()
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.armour += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]
