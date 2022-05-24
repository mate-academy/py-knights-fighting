class Knight:

    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def knight_armour(self, armour: list):
        for a in armour:
            self.protection += a["protection"]

    def knight_weapon(self, weapon: dict):
        self.power += weapon["power"]

    def knight_potion(self, potion: dict):
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
