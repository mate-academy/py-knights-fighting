class KnightConfig:
    def __init__(self, knight: dict ) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        for defence in knight["armour"]:
            self.protection += defence["protection"]

        self.power += knight["weapon"]["power"]

        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power = knight["potion"]["effect"]["power"]

            if "hp" in knight["potion"]["effect"]:
                self.hp = knight["potion"]["effect"]["hp"]

            if "protection" in knight["potion"]["effect"]:
                self.protection = knight["potion"]["effect"]["protection"]
