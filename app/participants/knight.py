class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0
        self.armour = knight_config["armour"]
        self.weapon = knight_config["weapon"]
        self.potion = knight_config["potion"]

    def apply_armour(self) -> None:
        for armour_item in self.armour:
            self.protection += armour_item["protection"]

    def apply_weapon(self) -> None:
        if self.weapon is not None:
            self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.power += self.potion["effect"].get("power", 0)
            self.hp += self.potion["effect"].get("hp", 0)
            self.protection += self.potion["effect"].get("protection", 0)
