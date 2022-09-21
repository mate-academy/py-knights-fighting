class Battle:
    def __init__(self, first,
                 second
                 ):
        self.first = first
        self.second = second

    def result_of_battle(self) -> None:
        self.first.hp -= self.second.power - self.first.protection
        self.second.hp -= self.first.power - self.second.protection
        if self.first.hp <= 0:
            self.first.hp = 0

        if self.second.hp <= 0:
            self.second.hp = 0

    def result_of_round(self) -> None:
        if self.first.hp > self.second.hp:
            print(f"{self.first.name} Destroys"
                  f" his opponent {self.second.name}")
        else:
            print(f"{self.second.name} Destroys"
                  f" his opponent {self.first.name}")
