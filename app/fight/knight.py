class Knight:
    knights = []

    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        Knight.knights.append(self)

    def apply_armor(self):
        for a in self.armour:
            self.protection += a['protection']

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
