class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def add_armour(self, armours: list) -> None:
        for armour in armours:
            self.protection += armour["protection"]

    def add_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def add_potion(self, potion: dict) -> None:
        if "power" in potion["effect"]:
            self.power += potion["effect"]["power"]
        if "hp" in potion["effect"]:
            self.hp += potion["effect"]["hp"]
        if "protection" in potion["effect"]:
            self.protection += potion["effect"]["protection"]
