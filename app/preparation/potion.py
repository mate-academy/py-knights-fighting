class Potion:
    def __init__(self, warrior: dict) -> None:
        self.warrior = warrior

    def use_potion(self) -> None:
        if self.warrior["potion"] is not None:
            if "power" in self.warrior["potion"]["effect"]:
                self.warrior["power"] \
                    += self.warrior["potion"]["effect"]["power"]

            if "protection" in self.warrior["potion"]["effect"]:
                self.warrior["protection"] \
                    += self.warrior["potion"]["effect"]["protection"]

            if "hp" in self.warrior["potion"]["effect"]:
                self.warrior["hp"] += self.warrior["potion"]["effect"]["hp"]
