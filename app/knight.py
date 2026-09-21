class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def battle_preparation(
        self, armour: list, weapon: dict, potion: dict
    ) -> None:
        self.protection = 0

        for piece in armour:
            self.protection = self.protection + piece["protection"]

        self.power += weapon["power"]

        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
