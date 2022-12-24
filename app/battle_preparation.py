class KnightPreparation:

    def __init__(self, knight_info: dict) -> None:
        self.knight_info = knight_info

    def apply_armour(self) -> None:
        self.knight_info["protection"] = 0
        for ar in self.knight_info["armour"]:
            self.knight_info["protection"] += ar["protection"]

    def apply_weapon(self) -> None:
        self.knight_info["power"] += self.knight_info["weapon"]["power"]

    def apply_potion(self) -> None:
        if self.knight_info["potion"] is not None:
            if "power" in self.knight_info["potion"]["effect"]:
                self.knight_info["power"] += \
                    self.knight_info["potion"]["effect"]["power"]

            if "protection" in self.knight_info["potion"]["effect"]:
                self.knight_info["protection"] += \
                    self.knight_info["potion"]["effect"]["protection"]

            if "hp" in self.knight_info["potion"]["effect"]:
                self.knight_info["hp"] += \
                    self.knight_info["potion"]["effect"]["hp"]

    def prepare_knight(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
