class Knight:

    def __init__(self, name: str, powr: int, hp: int,
                 arm: list, wep: dict, pot: dict, prot=0):
        self.name = name
        self.power = powr
        self.hp = hp
        self.armour = arm
        self.weapon = wep
        self.potion = pot
        self.protection = prot

    def char_stats(self):
        self.power += self.weapon["power"]
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
