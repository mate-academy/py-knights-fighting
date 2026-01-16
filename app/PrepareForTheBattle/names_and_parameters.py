class Stats:
    knights = {}

    def __init__(self, knights: dict):
        for key, value in knights.items():
            self.name = key
            self.parameters = value
            self.total_armor = 0
            self.total_power = value["power"]
            self.total_hp = value["hp"]
            self.knights[self.name] = {"hp": self.hp(), "power": self.power(),
                                       "armor": self.armour()}

    def armour(self):
        for armor in self.parameters["armour"]:
            self.total_armor += armor["protection"]
        if self.parameters["potion"] is not None:
            for key, value in self.parameters["potion"]["effect"].items():
                if key == "protection":
                    self.total_armor += value
            if self.total_armor is None:
                return 0
        return self.total_armor

    def power(self):
        self.total_power += self.parameters["weapon"]["power"]
        if self.parameters["potion"] is not None:
            for key, value in self.parameters["potion"]["effect"].items():
                if key == "power":
                    self.total_power += value
        return self.total_power

    def hp(self):
        if self.parameters["potion"] is not None:
            for key, value in self.parameters["potion"]["effect"].items():
                if key == "hp":
                    self.total_hp += value
        return self.total_hp
