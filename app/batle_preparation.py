class Preparation:
    power = 0
    protect = 0
    hp = 0

    def __init__(self, protection: dict):
        self.name = protection["name"]
        self.power = protection["power"]
        self.hp = protection["hp"]
        self.protection = protection
        self.armour()
        self.potion_if_exist()
        self.weapon()

    def armour(self):
        for temp in self.protection["armour"]:
            self.protect += temp["protection"]
        return self.protect

    def weapon(self):
        self.power += self.protection["weapon"]["power"]

    def potion_if_exist(self):

        if self.protection["potion"] is not None:

            if "power" in self.protection["potion"]["effect"]:
                self.power += self.protection["potion"]["effect"]["power"]

            if "protection" in self.protection["potion"]["effect"]:
                self.protect += \
                    self.protection["potion"]["effect"]["protection"]

            if "hp" in self.protection["potion"]["effect"]:
                self.hp += self.protection["potion"]["effect"]["hp"]
