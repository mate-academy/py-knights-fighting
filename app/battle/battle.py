class Battle:
    def __init__(self, knight_name1: dict, knight_name2: dict) -> None:
        self.knight_name1 = knight_name1
        self.knight_name2 = knight_name2

    def battle(self) -> None:
        self.knight_name1["hp"] -= (
            self.knight_name2["power"] - self.knight_name1["protection"])
        self.knight_name2["hp"] -= (
            self.knight_name1["power"] - self.knight_name2["protection"])

        if self.knight_name1["hp"] <= 0:
            self.knight_name1["hp"] = 0

        if self.knight_name2["hp"] <= 0:
            self.knight_name2["hp"] = 0
