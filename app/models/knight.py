class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0
        self.apply_armour(config.get("armour", []))
        self.apply_weapon(config["weapon"])
        self.apply_potion(config.get("potion"))

    def apply_armour(self, armour_list: list) -> None:
        for armour in armour_list:
            self.protection += armour["protection"]

    def apply_weapon(self, weapon: list) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: list) -> None:
        if potion and "effect" in potion:
            effects = potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
