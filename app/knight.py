class Knight:
    def __init__(self, configuration: dict) -> None:
        self.name = configuration["name"]
        self.power = configuration["power"] + configuration["weapon"]["power"]
        self.hp = configuration["hp"]
        self.protection = sum([armour["protection"]
                               for armour in configuration["armour"]])
        if configuration["potion"] is not None:
            if "power" in configuration["potion"]["effect"]:
                self.power += configuration["potion"]["effect"]["power"]
            if "protection" in configuration["potion"]["effect"]:
                self.protection += \
                    configuration["potion"]["effect"]["protection"]
            if "hp" in configuration["potion"]["effect"]:
                self.hp += configuration["potion"]["effect"]["hp"]
