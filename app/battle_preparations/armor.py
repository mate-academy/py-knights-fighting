class Armour:
    protection = 0

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

        for armor_protect in self.armour:
            self.protection += armor_protect["protection"]

        if self.potion is not None:
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
