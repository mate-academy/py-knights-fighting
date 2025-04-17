class BattlePreparation:

    def __init__(self, knight_name: dict) -> None:
        self.knight_name = knight_name

    def apply_armour(self) -> None:
        self.knight_name["protection"] = 0
        for item in self.knight_name["armour"]:
            self.knight_name["protection"] += item["protection"]

    def apply_weapon(self) -> None:
        self.knight_name["power"] += self.knight_name["weapon"]["power"]

    def apply_potion(self) -> None:
        if self.knight_name["potion"] is not None:
            if "power" in self.knight_name["potion"]["effect"]:
                self.knight_name["power"] += (
                    self.knight_name["potion"]["effect"]["power"])

            if "protection" in self.knight_name["potion"]["effect"]:
                self.knight_name["protection"] += (
                    self.knight_name["potion"]["effect"]["protection"])

            if "hp" in self.knight_name["potion"]["effect"]:
                self.knight_name["hp"] += (
                    self.knight_name["potion"]["effect"]["hp"])
