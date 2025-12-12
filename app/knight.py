class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.protection = 0
        self.configuration = config

    def set_weapon(self) -> None:
        self.power += self.configuration["weapon"]["power"]

    def set_armour(self) -> None:
        for arm in self.configuration["armour"]:
            self.protection += arm["protection"]

    def set_potion(self) -> None:
        if self.configuration["potion"] is not None:
            short = self.configuration["potion"]["effect"]
            self.power += short.get("power", 0)
            self.hp += short.get("hp", 0)
            self.protection += short.get("protection", 0)

    def prepare(self) -> None:
        self.set_weapon()
        self.set_armour()
        self.set_potion()
