class Knight:
    def __init__(self, configuration: dict) -> None:
        self.name = configuration["name"]
        self.hp = configuration["hp"]
        self.power = configuration["power"] + configuration["weapon"]["power"]
        self.protection = sum(
            part["protection"] for part in configuration["armour"]
        )
        potion = configuration.get("potion")
        if potion is not None:
            effects = potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
