class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")

        self.power = knight.get("power")
        self.hp = knight.get("hp")
        self.protection = 0

        self.armour = knight.get("armour")
        self.weapon = knight.get("weapon")
        self.potion = knight.get("potion")
