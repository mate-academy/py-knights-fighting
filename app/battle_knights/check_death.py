class CheckDeath:

    def __init__(self, warrior_1: dict, warrior_2: dict) -> None:
        self.warrior_1 = warrior_1
        self.warrior_2 = warrior_2

        if warrior_1["hp"] <= 0:
            warrior_1["hp"] = 0
        if warrior_2["hp"] <= 0:
            warrior_2["hp"] = 0
