class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = sum(item["protection"] for item in self.armour)

    def get_protection(self) -> int:
        return self.protection

    def get_power(self) -> int:
        return self.power + self.weapon["power"]

    def use_potion(self) -> None:
        if not self.potion:
            return

        effect = self.potion["effect"]
        if "hp" in effect:
            self.hp += effect["hp"]

        if "power" in effect:
            self.power += effect["power"]

        if "protection" in effect:
            self.protection += effect["protection"]
