class Knight:
    knights = dict()

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.protection = 0
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]
        self.weapon = knight["weapon"]["name"]
        self.armour = []
        Knight.knights[knight["name"]] = self
        if len(knight["armour"]) != 0:
            Knight.knight_armour(self, knight["armour"])
        if knight.get("potion"):
            setattr(self, "potion", knight["potion"])
            Knight.knight_potion(self, knight["potion"]["effect"])

    def knight_armour(self, armours: list[dict]) -> None:
        for armour in armours:
            self.armour.append(armour["part"])
            setattr(self, "protection", (getattr(self, "protection")
                                         + armour["protection"]))

    def knight_potion(self, potion: dict) -> None:
        for effect, value in potion.items():
            setattr(self, effect, (getattr(self, effect) + value))
