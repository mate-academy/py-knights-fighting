class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: list) -> None:
        for part in armour:
            self.protection += part["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return
        if "power" in potion["effect"]:
            self.power += potion["effect"]["power"]
        if "protection" in potion["effect"]:
            self.protection += potion["effect"]["protection"]
        if "hp" in potion["effect"]:
            self.hp += potion["effect"]["hp"]
