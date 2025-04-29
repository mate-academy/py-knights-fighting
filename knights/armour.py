class Armour:
    def __init__(self, armour_config: dict) -> None:
        self.part = armour_config["part"]
        self.protection = armour_config["protection"]
