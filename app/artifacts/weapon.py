class Weapon:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
