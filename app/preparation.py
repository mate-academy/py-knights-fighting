class Preparation:
    def __init__(self, knight: dict) -> None:
        self.knight = knight
        self.name = self.knight["name"]
        self.power = self.knight["power"]
        self.hp = self.knight["hp"]
        self.protection = self.knight["protection"]

    def armour(self):
        self.knight["protection"] = sum(
            protection_unit["protection"]
            for protection_unit in self.knight["armour"]
        )
        return Preparation(self.knight)

    def weapon(self):
        self.knight["power"] += self.knight["weapon"]["power"]
        return Preparation(self.knight)

    def potion(self):
        potion = self.knight["potion"]
        if potion is not None:
            for name, value in potion["effect"].items():
                self.knight[name] += value
        return Preparation(self.knight)
