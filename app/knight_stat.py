class Knight:
    def __init__(self, name, hp, power, armour, weapon, potion=None):
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def calculate_knight_stat(self):
        self.protection = 0

        for part in self.armour:
            self.protection += part["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            stat_list = ["power", "hp", "protection"]
            for stat in stat_list:
                if stat in self.potion["effect"]:
                    setattr(self, stat, getattr(self, stat) + self.potion["effect"][stat])

        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection
        }
