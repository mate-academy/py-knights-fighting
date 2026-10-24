class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.protection = 0
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]

    def prepare_for_battle(self) -> None:
        for data in self.armour:
            self.protection += data["protection"]
        self.power += self.weapon["power"]
        if self.potion:
            if "hp" in self.potion["effect"]:
                self.hp = self.hp + self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
