class Knight:
    list_knight = {}

    def __init__(self, name: str, config_k: dict) -> None:
        self.name = name
        self.config_power = config_k["power"] + config_k["weapon"]["power"]
        self.config_hp = config_k["hp"]
        self.config_armour = config_k["armour"]
        self.config_potion = config_k["potion"]
        Knight.list_knight[name] = self

    def config_preparations(self) -> None:
        sum_protection = 0
        for el_armour in self.config_armour:
            sum_protection += el_armour["protection"]
        if self.config_potion is not None:
            self.config_power += self.config_potion["effect"].get("power", 0)
            self.config_hp += self.config_potion["effect"].get("hp", 0)
            sum_protection += self.config_potion["effect"].get("protection", 0)
        self.config_armour = sum_protection
