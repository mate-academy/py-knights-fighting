class Knight:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.knight = self.stats[self.name]

    def get_hp(self):
        if self.knight["potion"] is not None:
            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]

        return self.knight["hp"]

    def get_power(self):
        self.knight["power"] += self.knight["weapon"]["power"]
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] += \
                    self.knight["potion"]["effect"]["power"]

        return self.knight["power"]

    def get_protection(self):
        self.knight["protection"] = 0
        for armour in self.knight["armour"]:
            self.knight["protection"] += armour["protection"]
        if self.knight["potion"] is not None:
            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] += \
                    self.knight["potion"]["effect"]["protection"]

        return self.knight["protection"]
