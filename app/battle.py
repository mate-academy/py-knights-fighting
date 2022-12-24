from app.battle_preparation import KnightPreparation


class Battle:

    def __init__(self, knight1: KnightPreparation,
                 knight2: KnightPreparation) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def battle(self) -> None:
        self.knight1.knight_info["hp"] -= \
            self.knight2.knight_info["power"] - \
            self.knight1.knight_info["protection"]

        self.knight2.knight_info["hp"] -= \
            self.knight1.knight_info["power"] - \
            self.knight2.knight_info["protection"]

        if self.knight1.knight_info["hp"] <= 0:
            self.knight1.knight_info["hp"] = 0

        if self.knight2.knight_info["hp"] <= 0:
            self.knight2.knight_info["hp"] = 0
