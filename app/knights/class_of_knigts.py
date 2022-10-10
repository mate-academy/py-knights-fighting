class Knights:
    def __init__(self, lord: dict) -> type(None):
        self.name = lord["name"]
        self.hp = lord["hp"]
        self.power = lord["power"]
        self.protection = 0
        self.armour = lord["armour"]
        self.weapon = lord["weapon"]
        self.potion = lord["potion"]

    def preparations(self) -> type(None):
        # apply armour
        for armo in self.armour:
            self.protection += armo["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
