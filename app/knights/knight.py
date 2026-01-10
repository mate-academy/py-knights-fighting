class Knight:
    def __init__(
        self,
        config: dict
    ) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.protection = 0

        self.add_protection(config["armour"])
        self.add_power(config["weapon"])
        self.apply_potion(config["potion"])

    def add_protection(self, armours: list[dict]) -> None:
        for armour in armours:
            self.protection += armour["protection"]

    def add_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
