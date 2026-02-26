class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"] + knight_config["weapon"]["power"]
        self.hp = knight_config["hp"]
        self.armour = knight_config["armour"]
        self.weapon = knight_config["weapon"]
        self.potion = knight_config["potion"]
        self.protection = sum(armour["protection"] for armour in self.armour)

        self.add_potion()

    def add_potion(self) -> None:
        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
