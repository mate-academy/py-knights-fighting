class Weapon:

    possible_weapon = {}

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.__class__.possible_weapon[name] = self

    def apply_weapon(self, knight):
        knight.power += self.power
