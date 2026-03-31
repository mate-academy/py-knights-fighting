class Knight:
    dict_of_knights = {}

    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info.get("name")
        self.power = knight_info.get("power")
        self.hp = knight_info.get("hp")
        self.armour = knight_info.get("armour")
        self.weapon = knight_info.get("weapon")
        self.potion = knight_info.get("potion")
        self.protection = 0
        Knight.dict_of_knights[self.name] = self
