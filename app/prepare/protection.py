class Protection:
    def __init__(self, knight: dict):
        self.knight = knight
        self.knight["protection"] = 0

    def get_protection(self):
        for a in self.knight["armour"]:
            self.knight["protection"] += a["protection"]

    def get_weapon(self):
        self.knight["power"] += self.knight["weapon"]["power"]

    def get_potion(self):
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] +=\
                    self.knight["potion"]["effect"]["power"]

            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] +=\
                    self.knight["potion"]["effect"]["protection"]

            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
