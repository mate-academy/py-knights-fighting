class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.protection = 0

        self.apply_armour(config["armour"])
        self.apply_weapon(config["weapon"])
        self.apply_potion(config["potion"])

    def apply_armour(self, armour: list) -> None:
        for part_of_armour in armour:
            self.protection += part_of_armour["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            for key, value in potion["effect"].items():
                if hasattr(self, key):
                    setattr(self, key, getattr(self, key) + value)
