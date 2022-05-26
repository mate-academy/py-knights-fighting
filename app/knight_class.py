class Knight:
    def __init__(self, knight):
        self.name = knight["name"]
        self.protection = 0
        self.power = knight["power"]
        self.hp = knight["hp"]

        # apply armour
        for a in knight["armour"]:
            self.protection += a["protection"]

        # apply weapon
        self.power += knight["weapon"]["power"]

        # apply potion if exist
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                self.protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                self.hp += knight["potion"]["effect"]["hp"]
