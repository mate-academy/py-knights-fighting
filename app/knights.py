class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.protection = 0
        self.armour = data["armour"]
        self.weapon = data["weapon"]
        self.potion = data["potion"]

    def buff(self) -> None:
        self.protection = sum(obj["protection"] for obj in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effects = self.potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
