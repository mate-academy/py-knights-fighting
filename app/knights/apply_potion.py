class Potion:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_potion(self) -> dict:
        for hero in self.knight:
            if self.knight[hero]["potion"] is not None:
                Potion(self.knight[hero]).add_parameters()
        return self.knight

    def add_parameters(self) -> dict:
        if "power" in self.knight["potion"]["effect"]:
            self.knight["power"] += self.knight["potion"]["effect"]["power"]

        if "protection" in self.knight["potion"]["effect"]:
            self.knight["protection"] += \
                self.knight["potion"]["effect"]["protection"]

        if "hp" in self.knight["potion"]["effect"]:
            self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
        return self.knight
