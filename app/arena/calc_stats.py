class KnightStat:

    def __init__(self, other):
        self.stat = other
        self.hp = other["hp"]
        self.power = other["power"]
        self.protection = 0
        self.name = other["name"]
        self.clothes = other["armour"]
        self.potions = other["potion"]
        self.weapon = other["weapon"]

    def calc_stats(self):
        for arm in self.clothes:
            for key, value in arm.items():
                if key == "protection":
                    self.protection += value
        self.power += self.weapon["power"]
        if self.potions is not None:
            for key, value in self.potions["effect"].items():
                if key == "power":
                    self.power += value
                elif key == "hp":
                    self.hp += value
                elif key == "protection":
                    self.protection += value
        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection
        }
