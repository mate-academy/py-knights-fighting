class Potion:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_potion(self) -> dict:
        for hero in self.knight:
            if self.knight[hero]["potion"] is not None:
                Potion(self.knight[hero]).power()
                Potion(self.knight[hero]).protection()
                Potion(self.knight[hero]).hp()
        return self.knight

    def power(self) -> dict:
        if "power" in self.knight["potion"]["effect"]:
            self.knight["power"] += self.knight["potion"]["effect"]["power"]
            return self.knight

    def protection(self) -> dict:
        if "protection" in self.knight["potion"]["effect"]:
            self.knight["protection"] += \
                self.knight["potion"]["effect"]["protection"]
            return self.knight

    def hp(self) -> dict:
        if "hp" in self.knight["potion"]["effect"]:
            self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
            return self.knight
