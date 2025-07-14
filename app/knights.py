class Knight:
    def __init__(self, config: dict):
        self.protection = None
        self.power = None
        self.name = config["name"]
        self.base_power = config["power"]
        self.hp = config["hp"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")

        self.apply_gear()

    def apply_gear(self):
        self.power = self.base_power + self.weapon["power"]
        self.protection = sum(part["protection"] for part in self.armour)
        if self.potion:
            for stat, effect in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + effect)

    def receive_damage(self, damage: int):
        self.hp = max(0, self.hp - damage)
