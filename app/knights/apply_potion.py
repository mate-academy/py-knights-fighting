class Potion:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_potion(self) -> dict:

        for hero in self.knight:
            if self.knight[hero]["potion"] is not None:
                if "power" in self.knight[hero]["potion"]["effect"]:
                    self.knight[hero]["power"] += \
                        self.knight[hero]["potion"]["effect"]["power"]

                if "protection" in self.knight[hero]["potion"]["effect"]:
                    self.knight[hero]["protection"] += \
                        self.knight[hero]["potion"]["effect"]["protection"]

                if "hp" in self.knight[hero]["potion"]["effect"]:
                    self.knight[hero]["hp"] += \
                        self.knight[hero]["potion"]["effect"]["hp"]

        return self.knight
