class Knight:
    def __init__(self, config):
        self.protection = 0
        self.power = config["power"]
        self.name = config["name"]
        self.hp = config["hp"]
        self.apply_weapon(config)
        self.apply_armour(config)
        self.apply_potion(config)

    def apply_armour(self, config: dict) -> None:
        if armour := config.get("armour"):
            self.protection += sum([item["protection"] for item in armour])

    def apply_weapon(self, config) -> None:
        if weapon := config.get("weapon"):
            self.power += weapon["power"]

    def apply_potion(self, config):
        if potion := config.get("potion"):
            potion_effect = potion.get("effect")
            self.power += potion_effect.get("power")
            self.hp += potion_effect.get("hp")
            self.protection += potion_effect.get("protection")


