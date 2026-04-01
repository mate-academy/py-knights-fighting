class Knight:
    def __init__(self, knight_attr: dict) -> None:
        self.name = knight_attr.get("name")
        self.power = knight_attr.get("power")
        self.hp = knight_attr.get("hp")
        self.armour = knight_attr.get("armour")
        self.weapon = knight_attr.get("weapon")
        self.potion = knight_attr.get("potion")
        self.protection = 0

    @classmethod
    def create_knights_from_data(cls, attrs: dict) -> dict:
        knight_dict = {}
        for knight_data in attrs.values():
            knight_dict.update({knight_data.get("name"): Knight(knight_data)})

        return knight_dict
