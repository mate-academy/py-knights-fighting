class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")

        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        self.protection = sum(item["protection"] for item in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)
