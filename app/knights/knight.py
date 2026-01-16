class Knight:

    def __init__(self, config: dict) -> None:

        self.name = config.get("name")
        self.power = config.get("power")
        self.hp = config.get("hp")
        self.protection = 0

        if config["armour"] and len(config["armour"]) > 0:
            for item in config["armour"]:
                self.protection += item["protection"]

        if config["weapon"]["power"]:
            self.power += config["weapon"]["power"]

        if config["potion"] and config["potion"]["effect"]:
            if "power" in config["potion"]["effect"]:
                self.power += config["potion"]["effect"]["power"]

            if "hp" in config["potion"]["effect"]:
                self.hp += config["potion"]["effect"]["hp"]

            if "protection" in config["potion"]["effect"]:
                self.protection += config["potion"]["effect"]["protection"]
