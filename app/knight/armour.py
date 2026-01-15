class Armour:
    def __init__(self, armour: list):
        self.armour = armour
        self.protection = 0

    def use_armour(self):
        for thing in self.armour:
            self.protection += thing["protection"]
        return self.protection
