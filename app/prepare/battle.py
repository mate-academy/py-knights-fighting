class Battle:
    def __init__(self, knight):
        self.knight = knight

    def battle_knight(self, other: dict):
        self.knight["hp"] -= other["power"] - self.knight["protection"]
        other["hp"] -= self.knight["power"] - other["protection"]

        if self.knight["hp"] <= 0:
            self.knight["hp"] = 0

        if other["hp"] <= 0:
            other["hp"] = 0
