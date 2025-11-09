from app.knight.knight import Knight


class Character(Knight):
    def __init__(self, name: str, power: int, hp: int):
        super().__init__(name, power, hp)
        self.armour = []
        self.weapon = None
        self.potion = None
        self.protection = 0

    def equip_character(self, config: dict) -> None:
        self.weapon = config[self.name]["weapon"]
        self.potion = config[self.name]["potion"]
        self.armour = config[self.name]["armour"]

