class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon["name"]
        self.power = weapon["power"]
