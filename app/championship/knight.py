class Knight:
    def __init__(self, knight_dict: dict) -> None:
        self.name = knight_dict["name"]
        self.hp = knight_dict["hp"]
        self.power = knight_dict["power"]
        self.armours = knight_dict["armour"]
        self.weapon = knight_dict["weapon"]
        self.potion = knight_dict["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        for armor in self.armours:
            self.protection += armor["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:

            for effect, value in self.potion["effect"].items():
                if effect == "power":
                    self.power += value

                if effect == "protection":
                    self.protection += value

                if effect == "hp":
                    self.hp += value

    def preparation(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
