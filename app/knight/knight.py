class Knight:
    def __init__(self, knights_config: dict) -> None:
        self.knights_config = knights_config
        self.name = knights_config["name"]
        self.hp = self.knights_config["hp"]
        self.power = (
            self.knights_config["power"]
            + self.knights_config["weapon"]["power"]
        )
        self.protection = 0

    def calculate_stats(self) -> None:
        self.protection = self.apply_armour()
        self.apply_potion()

    def apply_armour(self) -> int:
        return sum(
            armour["protection"] for armour in self.knights_config["armour"]
        )

    def apply_potion(self) -> None:
        if self.knights_config["potion"]:
            if "hp" in self.knights_config["potion"]["effect"]:
                self.hp += self.knights_config["potion"]["effect"]["hp"]
            if "power" in self.knights_config["potion"]["effect"]:
                self.power += self.knights_config["potion"]["effect"]["power"]
            if "protection" in self.knights_config["potion"]["effect"]:
                self.protection += (
                    self.knights_config)["potion"]["effect"]["protection"]
