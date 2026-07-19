class Knight:
    def __init__(self, knight_dict: dict) -> None:
        self.name = knight_dict["name"]
        self.power = knight_dict["power"] + knight_dict["weapon"]["power"]
        self.hp = knight_dict["hp"]
        self.armour = sum(a["protection"] for a in knight_dict["armour"])
        self.potion = knight_dict["potion"]
        self.apply_potion()

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.armour += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
