class Battle:
    battles_result = {"Lancelot": 0,
                      "Arthur": 0,
                      "Mordred": 0,
                      "Red Knight": 0}

    def __init__(self, knight_1: dict, knight_2: dict) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def fight(self) -> None:
        knight_2_damage = self.knight_2["power"] - self.knight_1["protection"]
        knight_1_damage = self.knight_1["power"] - self.knight_2["protection"]
        self.knight_1["hp"] -= knight_2_damage
        self.knight_2["hp"] -= knight_1_damage

        if self.knight_1["hp"] <= 0:
            self.knight_1["hp"] = 0
        if self.knight_2["hp"] <= 0:
            self.knight_2["hp"] = 0

        self.battles_result.update({
            self.knight_1["name"]: self.knight_1["hp"],
            self.knight_2["name"]: self.knight_2["hp"],
        })
