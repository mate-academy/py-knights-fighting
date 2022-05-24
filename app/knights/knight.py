class Knight:
    def __init__(self, knight: dict):
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def battle_preparation(self):
        # apply armour
        self.protection = 0
        for a in self.armour:
            self.protection += a["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def start_battle(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
