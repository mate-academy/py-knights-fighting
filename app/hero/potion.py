class Potion:
    def __init__(self, potion: dict):
        self.name = None
        self.power = 0
        self.hp = 0
        self.protection = 0

        if potion:
            self.name = potion["name"]

            if "power" in potion["effect"]:
                self.power = potion["effect"]["power"]

            if "hp" in potion["effect"]:
                self.hp = potion["effect"]["hp"]

            if "protection" in potion["effect"]:
                self.protection = potion["effect"]["protection"]
