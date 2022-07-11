class Power:

    def __init__(self, knight: dict):
        self.knight = knight

    def battle_power(self):

        # apply weapon
        self.knight["power"] += self.knight["weapon"]["power"]
        # apply potion if exist
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] += self.knight["potion"]["effect"]["power"]
        return self.knight["power"]
