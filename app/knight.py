class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0
        self.power += config["weapon"]["power"]

        for armour in config["armour"]:
            self.protection += armour["protection"]

        if config["potion"] is not None:
            for stat, value in config["potion"]["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)
