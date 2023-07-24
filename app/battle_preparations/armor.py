class Armour:
    protection = 0

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.armour = knight["armour"]
        self.potion = knight["potion"]
        knight["protection"] = 0

        for armor_protect in self.armour:
            self.protection += armor_protect["protection"]

        if self.potion is not None:
            for i in self.potion["effect"]:
                knight[i] += self.potion["effect"][i]

        self.protection += knight["protection"]
        self.hp = knight["hp"]
        self.power = knight["power"] + knight["weapon"]["power"]
