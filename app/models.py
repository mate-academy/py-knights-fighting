class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")

        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = sum(part["protection"] for part in self.armour)

        self.apply_weapon()
        self.apply_potion()


    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effects = self.potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
