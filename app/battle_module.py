class Battle:
    def __init__(self, pair: tuple):
        self.knight_1 = pair[0]
        self.knight_2 = pair[1]

    def result(self):
        self.knight_1["hp"] -= \
            self.knight_2["power"] - self.knight_1["protection"]
        self.knight_2["hp"] -= \
            self.knight_1["power"] - self.knight_2["protection"]

        # check if someone fell in battle
        if self.knight_1["hp"] <= 0:
            self.knight_1["hp"] = 0

        if self.knight_2["hp"] <= 0:
            self.knight_2["hp"] = 0

        return {self.knight_1["name"]: self.knight_1["hp"],
                self.knight_2["name"]: self.knight_2["hp"]
                }
