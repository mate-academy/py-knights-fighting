class Knight:
    def __init__(self, name, power, hp, armours, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def applying(self):
        for armour in self.armours:
            self.protection += armour["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                if self.potion["effect"]["hp"] > 0:
                    self.hp += self.potion["effect"]["hp"]
                if self.potion["effect"]["hp"] < 0:
                    self.power += abs(self.potion["effect"]["hp"])
