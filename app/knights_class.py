class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.protection = 0
        self.power = data["power"]
        self.hp = data["hp"]
        self.calc_stats(data)

    def calc_stats(self, data: dict) -> None:
        self.power += data["weapon"]["power"]
        if data["armour"]:
            self.protection = sum(item["protection"]
                                  for item in data["armour"])
        if data["potion"]:
            for stat in (["power", "hp", "protection"]):
                self.__dict__[stat] += data["potion"]["effect"].get(stat, 0)
