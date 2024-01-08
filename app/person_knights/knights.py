class Knights:

    def __init__(self, knights_config: dict) -> None:
        self.name: str = knights_config["name"]
        self.power = knights_config["power"]
        self.hp = knights_config["hp"]
        self.armour: list[dict] = knights_config["armour"]
        self.weapon: dict = knights_config["weapon"]
        self.potion: dict = knights_config["potion"]
        self.protection = 0

    def battle_preparations(self) -> None:

        # apply armour
        for arm in self.armour:
            self.protection += arm["protection"]

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
