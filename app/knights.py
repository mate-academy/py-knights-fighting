class Knight:

    def __init__(self, info: dict) -> None:
        self.name = info["name"]
        self.power = info["power"]
        self.hp = info["hp"]
        self.armour = info["armour"]
        self.weapon = info["weapon"]
        self.potion = info["potion"]

    def knight_protection(self) -> None:
        self.protection = 0
        for staff in self.armour:
            for item in list(staff.values()):
                if isinstance(item, (int, float)):
                    self.protection += item

    def knight_power(self) -> None:
        for item in self.weapon.values():
            if isinstance(item, (int, float)):
                self.power += item

    def knight_poution(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def knight_stats(self) -> dict:
        self.knight_protection()
        self.knight_power()
        self.knight_poution()
        return {"hp": self.hp, "power": self.power,
                "protection": self.protection}
