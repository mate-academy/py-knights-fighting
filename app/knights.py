class KnightClass:
    def __init__(self, knight: dict):
        self.knight = knight

    def name(self):
        return self.knight["name"]

    def protection(self):
        self.knight["protection"] = 0
        for a in self.knight["armour"]:
            self.knight["protection"] += a["protection"]
        if self.knight["potion"] is not None:
            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] += \
                    self.knight["potion"]["effect"]["protection"]
        return self.knight["protection"]

    def power(self):
        self.knight["power"] += self.knight["weapon"]["power"]
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] += \
                    self.knight["potion"]["effect"]["power"]
        return self.knight["power"]

    def hp(self):
        if self.knight["potion"] is not None:
            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
        return self.knight["hp"]
