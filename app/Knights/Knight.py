class Knight:
    def __init__(self, knights_dict: dict) -> None:
        self.name = knights_dict["name"]
        self.power = knights_dict["power"]
        self.hp = knights_dict["hp"]
        self.armour = knights_dict["armour"]
        self.weapon = knights_dict["weapon"]
        self.potion = knights_dict["potion"]

    def preparing_of_knight(self) -> None:
        if self.armour:
            self.armour = sum(element["protection"] for element in self.armour)
        else:
            self.armour = 0

        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.armour += effect.get("protection", 0)
