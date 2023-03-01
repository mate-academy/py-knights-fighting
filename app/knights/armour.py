class Armour:

    possible_armour = {}

    def __init__(self, part, protection):
        self.part = part
        self.protection = protection
        self.__class__.possible_armour[f"{part}_{protection}"] = self

    def apply_armour(self, knight):
        knight.protection += self.protection
