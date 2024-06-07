class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.protection = 0
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def modify_knight(self) -> None:
        self.power += self.weapon["power"]
        for part_of_armour in self.armour:
            self.protection += part_of_armour["protection"]

        if self.potion:
            self.power += self.potion["effect"].get("power", 0)
            self.hp += self.potion["effect"]["hp"]
            self.protection += self.potion["effect"].get("protection", 0)
