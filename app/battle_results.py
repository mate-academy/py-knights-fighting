class BattleResults:
    def __init__(self, fighter1: object, fighter2: object) -> None:
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def health_check(self, health) -> int:
        if health < 0:
            health = 0
        return health

    def battle_results(self) -> tuple:
        self.fighter1.hp -= self.fighter2.power - self.fighter1.protection
        self.fighter2.hp -= self.fighter1.power - self.fighter2.protection

        self.fighter1.hp = self.health_check(self.fighter1.hp)
        self.fighter2.hp = self.health_check(self.fighter2.hp)
        return (self.fighter1.hp, self.fighter2.hp)
