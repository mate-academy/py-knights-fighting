class Tournament:
    def __init__(self, king: dict) -> None:
        self.king = king

    def configurations(self) -> None:
        self.king["protection"] = 0
        for protect in self.king["armour"]:
            self.king["protection"] += protect["protection"]

        # apply weapon
        self.king["power"] += self.king["weapon"]["power"]

        # apply potion if exist
        if self.king["potion"] is not None:
            if "power" in self.king["potion"]["effect"]:
                self.king["power"] += self.king["potion"]["effect"]["power"]

            if "protection" in self.king["potion"]["effect"]:
                self.king["protection"] +=\
                    self.king["potion"]["effect"]["protection"]

            if "hp" in self.king["potion"]["effect"]:
                self.king["hp"] += self.king["potion"]["effect"]["hp"]

    def battle(self, knight2: dict) -> None:
        self.king["hp"] -= knight2["power"] - self.king["protection"]
        knight2["hp"] -= self.king["power"] - knight2["protection"]
        if self.king["hp"] <= 0:
            self.king["hp"] = 0

        if knight2["hp"] <= 0:
            knight2["hp"] = 0
