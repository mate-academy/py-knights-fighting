class Battle:

    def __init__(self, first_knight, second_knight):
        self.first_knight = first_knight
        self.second_knight = second_knight

    def battle(self):
        power_1 = self.first_knight["power"]
        power_2 = self.second_knight["power"]
        protection_1 = self.first_knight["protection"]
        protection_2 = self.second_knight["protection"]
        self.first_knight["hp"] -= power_2 - protection_1
        self.second_knight["hp"] -= power_1 - protection_2

    # check if someone fell in battle
        if self.first_knight["hp"] <= 0:
            self.first_knight["hp"] = 0

        if self.second_knight["hp"] <= 0:
            self.second_knight["hp"] = 0
