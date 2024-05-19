class Knight:
    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.weapon = knight_info["weapon"]
        self.hp = knight_info["hp"]
        self.armour = knight_info["armour"]
        self.potion = knight_info["potion"]
        self.power = knight_info["power"] + self.weapon["power"]
        self.protection = sum(
            armor_part["protection"]
            for armor_part in self.armour
        )
        self.apply_potion()

    def apply_potion(self) -> None:
        if self.potion:
            for effect, value in self.potion["effect"].items():
                setattr(self, effect, value + getattr(self, effect))
