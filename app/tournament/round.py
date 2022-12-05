class Round:
    def __init__(self, player_1: dict, player_2: dict) -> None:
        self.player_1 = player_1
        self.player_2 = player_2

    def round(self) -> tuple:
        self.player_1["hp"] -= self.player_2["power"] - \
            self.player_1["protection"]
        self.player_2["hp"] -= self.player_1["power"] - \
            self.player_2["protection"]

        return self.player_1, self.player_2
