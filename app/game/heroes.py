class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.power: int = config["power"]
        self.hp: int = config["hp"]
        self.weapon: dict = config["weapon"]
        self.armour: list[dict] = config["armour"]
        self.potion: dict = config.get("potion")
        self.protection = 0

    def apply_armour(self) -> None:
        for part_of_armour in self.armour:
            self.protection += part_of_armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            for stat, effect in self.potion["effect"].items():
                if stat == "hp":
                    self.hp += effect
                elif stat == "power":
                    self.power += effect
                elif stat == "protection":
                    self.protection += effect
