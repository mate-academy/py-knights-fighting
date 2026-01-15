from typing import List


class Battle:
    def __init__(self, knight_first: dict, knight_second: dict) -> None:
        self.first = knight_first
        self.second = knight_second

    def run_battle(self) -> List[dict]:
        self.first["hp"] -= self.second["power"] - self.first["protection"]
        self.second["hp"] -= self.first["power"] - self.second["protection"]

        # check if someone fell in battle
        if self.first["hp"] <= 0:
            self.first["hp"] = 0

        if self.second["hp"] <= 0:
            self.second["hp"] = 0

        return [self.first, self.second]
