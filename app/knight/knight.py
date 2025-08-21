class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.power = knight["power"] + self.weapon["power"]
        self.protection = sum(element.get("protection")
                              for element in self.armour)

    def drink_potion(self, potion: dict) -> None:
        if potion:
            potion = potion["effect"]
            if potion.get("power") is not None:
                self.power += potion.get("power", 0)
            if potion.get("hp") is not None:
                self.hp += potion.get("hp", 0)
            if potion.get("protection") is not None:
                self.protection += potion.get("protection", 0)

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0
