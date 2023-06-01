class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.protection = 0
        self.power = power

    def __str__(self) -> str:
        return f"name: {self.name}, hp: {self.hp}, " \
               f"protection: {self.protection}, power: {self.power}"

    def set_protection(self, armours: list) -> None:
        for armour in armours:
            self.protection += armour["protection"]

    def set_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def set_potion(self, potion: dict) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
