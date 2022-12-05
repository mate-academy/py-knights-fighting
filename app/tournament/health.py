class Health:
    def __init__(self, hp_1: dict, hp_2: dict) -> None:
        self.hp_1 = hp_1
        self.hp_2 = hp_2

    def health(self) -> tuple:
        if self.hp_1["hp"] < 0:
            self.hp_1["hp"] = 0
        if self.hp_2["hp"] < 0:
            self.hp_2["hp"] = 0

        return self.hp_1, self.hp_2
