class Knight:
    list_knight = {}

    def __init__(self, name: str, config_knight: dict) -> None:
        self.name = name
        self.power = config_knight["power"] + config_knight["weapon"]["power"]
        self.hp = config_knight["hp"]
        self.armour = config_knight["armour"]
        self.potion = config_knight["potion"]
        Knight.list_knight[name] = self

    def config_preparations(self) -> None:
        sum_protection = 0
        for el_armour in self.armour:
            sum_protection += el_armour["protection"]
        if self.potion is not None:
            self.power += self.potion["effect"].get("power", 0)
            self.hp += self.potion["effect"].get("hp", 0)
            sum_protection += self.potion["effect"].get("protection", 0)
        self.armour = sum_protection
