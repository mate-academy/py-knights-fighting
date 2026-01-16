class Knight:
    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.protection = 0
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.armour = knight_info["armour"]
        self.weapon = knight_info["weapon"]
        self.potion = knight_info["potion"]

    def calculate_protection(self) -> None:
        if self.armour:
            for item in self.armour:
                self.protection += item["protection"]

    def calculate_power(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
