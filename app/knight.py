class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.count_armour(armour)
        self.count_weapon(weapon)
        self.count_potion(potion)

    def count_armour(self, armour):
        for part in armour:
            self.protection += part["protection"]

    def count_weapon(self, weapon):
        self.power += weapon["power"]

    def count_potion(self, potion):
        if potion:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
