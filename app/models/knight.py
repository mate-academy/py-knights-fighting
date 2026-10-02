class Knight:

    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.protection = sum(a["protection"] for a in knight_data["armour"])
        self.power += knight_data["weapon"]["power"]
        potion = knight_data.get("potion")
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
