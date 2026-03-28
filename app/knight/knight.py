class Knight:
    def __init__(self, knight_character: dict) -> None:
        self.name = knight_character["name"]
        self.power = knight_character["power"]
        self.hp = knight_character["hp"]
        self.protection = 0
        self.armour = knight_character["armour"]
        self.weapon = knight_character["weapon"]
        self.potion = knight_character["potion"]
