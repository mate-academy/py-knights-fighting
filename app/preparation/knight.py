class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: list) -> int:
        for part in armour:
            self.protection += part["protection"]
        return self.protection

    def apply_weapon(self, weapon: dict) -> int:
        self.power += weapon["power"]
        return self.power

    def apply_potion(self, potion: dict) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
