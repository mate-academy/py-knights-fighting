class Battle:
    def __init__(self, first_knight: dict, second_knight: dict) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def battle(self) -> None:
        self.first_knight["hp"] -= (self.second_knight["power"]
                                    - self.first_knight["protection"])
        self.second_knight["hp"] -= (self.first_knight["power"]
                                     - self.second_knight["protection"])

        if self.first_knight["hp"] <= 0:
            self.first_knight["hp"] = 0

        if self.second_knight["hp"] <= 0:
            self.second_knight["hp"] = 0
