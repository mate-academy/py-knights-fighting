class Fighter:
    def __init__(
            self,
            config: dict
    ) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = 0
        self.apply_weapon()
        self.apply_armour()
        self.apply_potion()

    def apply_armour(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)
            self.hp += self.potion["effect"].get("hp", 0)
