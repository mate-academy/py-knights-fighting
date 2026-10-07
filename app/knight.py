class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"] + config["weapon"]["power"]
        self.protection = sum(
            armour["protection"] for armour in config["armour"]
        )

        if config["potion"] is not None:
            effects = config["potion"]["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def receive_hit(self, opponent: "Knight") -> None:
        damage = opponent.power - self.protection
        self.hp = max(0, self.hp - damage)
