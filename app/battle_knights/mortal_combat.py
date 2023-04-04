class Combat:

    def __init__(self, warrior_1: dict, warrior_2: dict) -> None:
        self.warrior_1 = warrior_1
        self.warrior_2 = warrior_2

        self.warrior_1["hp"] -= \
            self.warrior_2["power"] - self.warrior_1["protection"]
        self.warrior_2["hp"] -= \
            self.warrior_1["power"] - self.warrior_2["protection"]
