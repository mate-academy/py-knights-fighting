class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: dict, potion: dict):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @staticmethod
    def create_character(stats):
        return Knight(name=stats["name"], power=stats["power"], hp=stats["hp"],
                      armour=stats["armour"], weapon=stats["weapon"], potion=stats["potion"])

    def apply_armour(self):
        for a in self.armour:
            self.protection += a["protection"]

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