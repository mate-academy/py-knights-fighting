class Knight:
    def __init__(self, dict_knight: dict) -> None:
        self.name = dict_knight["name"]
        self.hp = dict_knight["hp"]
        self.power = dict_knight["power"] + dict_knight["weapon"]["power"]
        self.protection = sum(
            [armour["protection"] for armour in dict_knight["armour"]]
        )
        self.drink_the_potion(dict_knight["potion"])

    def drink_the_potion(self, potion: dict) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
