class Knight:
    def __init__(self, config):
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = self.apply_armour()
        self.power += self.weapon["power"]
        self.apply_potion()

    def apply_armour(self):
        protection = 0
        for a in self.armour:
            protection += a["protection"]
        return protection

    def apply_potion(self):
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def battle(self, opponent):
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp <= 0:
            self.hp = 0

        if opponent.hp <= 0:
            opponent.hp = 0
