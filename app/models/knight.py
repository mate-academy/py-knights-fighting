class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]

        self.apply_armour(config["armour"])
        self.apply_weapon(config["weapon"])
        self.apply_potion(config["potion"])

    def apply_armour(self, armour: list) -> None:
        self.protection = sum(
            item["protection"] for item in armour
        )

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return

        for stat, value in potion["effect"].items():
            setattr(self, stat, getattr(self, stat) + value)
