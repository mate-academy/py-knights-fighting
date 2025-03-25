class Armour:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion=None):
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.power = self.calculate_power()
        self.protection = self.calculate_protection()

    def calculate_power(self):
        power = self.base_power + self.weapon.power
        if self.potion and "power" in self.potion.effect:
            power += self.potion.effect["power"]
        return power

    def calculate_protection(self):
        protection = sum(a.protection for a in self.armour)
        if self.potion and "protection" in self.potion.effect:
            protection += self.potion.effect["protection"]
        return protection

    def apply_potion_effects(self):
        if self.potion and "hp" in self.potion.effect:
            self.hp += self.potion.effect["hp"]

    def take_damage(self, damage):
        self.hp -= max(0, damage - self.protection)
        self.hp = max(0, self.hp)
