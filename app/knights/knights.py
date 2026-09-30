class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.protection = 0
        self.power = config["power"]

        # apply armour
        for arm in config["armour"]:
            self.protection += arm["protection"]

        # apply weapon
        self.power += config["weapon"]["power"]

        # apply potion if exist
        if config["potion"] is not None:
            if "power" in config["potion"]["effect"]:
                self.power += config["potion"]["effect"]["power"]

            if "protection" in config["potion"]["effect"]:
                self.protection += config["potion"]["effect"]["protection"]

            if "hp" in config["potion"]["effect"]:
                self.hp += config["potion"]["effect"]["hp"]
