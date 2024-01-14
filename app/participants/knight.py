class Knight:

    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = self.apply_armour(knight_config["armour"])

        self.apply_weapon(knight_config["weapon"])
        self.apply_potion(knight_config["potion"])

    def apply_armour(self, armour_config: list) -> int:
        return sum(item["protection"] for item in armour_config)

    def apply_weapon(self, weapon_config: dict) -> None:
        self.power += weapon_config["power"]

    def apply_potion(self, potion_config: dict) -> None:
        if potion_config is None:
            return

        effects = potion_config["effect"]

        for key, value in effects.items():
            setattr(self, key, getattr(self, key) + value)
