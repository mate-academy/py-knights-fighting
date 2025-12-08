class BattleFight:
    def __init__(self, fighter1: dict, fighter2: dict) -> None:
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def battle(self) -> None:
        self.fighter1["hp"] -= self.fight(self.fighter2, self.fighter1)
        self.fighter2["hp"] -= self.fight(self.fighter1, self.fighter2)

        if self.fighter1["hp"] <= 0:
            self.fighter1["hp"] = 0

        if self.fighter2["hp"] <= 0:
            self.fighter2["hp"] = 0

    @staticmethod
    def fight(first_fighter: dict, second_fighter: dict) -> int:
        return first_fighter["power"] - second_fighter["protection"]

    def get_fighters_hp(self) -> tuple:
        return self.fighter1, self.fighter2
