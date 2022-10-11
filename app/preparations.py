class Preparation:

    def __init__(self, knight):
        self.knight = knight

    def apply_armour(self):
        self.knight["protection"] = 0
        for a in self.knight["armour"]:
            self.knight["protection"] += a["protection"]

    def apply_weapon(self):
        self.knight["power"] += self.knight["weapon"]["power"]

    def apply_potion_if_exist(self):
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] += \
                    self.knight["potion"]["effect"]["power"]

            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] += \
                    self.knight["potion"]["effect"]["protection"]

            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
