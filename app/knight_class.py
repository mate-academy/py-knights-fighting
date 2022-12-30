class Knight:
    def __init__(self, dict_knight: dict) -> None:
        self.name = dict_knight["name"]
        self.hp = dict_knight["hp"]
        self.power = dict_knight["power"] + dict_knight["weapon"]["power"]
        self.protection = sum(
            [armour["protection"] for armour in dict_knight["armour"]]
        )
        self.potion = dict_knight["potion"]

    def drink_the_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
