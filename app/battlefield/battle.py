from app.characters.knight import Knight


class Battle:
    fighters = []

    def __init__(self, first: Knight, second: Knight) -> None:
        self.first = first
        self.second = second
        Battle.fighters.extend([self.first, self.second])

    def fight(self) -> None:
        self.first.hp -= self.second.power - self.first.protection
        self.second.hp -= self.first.power - self.second.protection
        self.check_for_hp()

    def check_for_hp(self) -> None:
        if self.first.hp <= 0:
            self.first.hp = 0
        if self.second.hp <= 0:
            self.second.hp = 0

    @classmethod
    def get_result(cls) -> dict:
        result = {}
        for fighter in cls.fighters:
            result[fighter.name] = fighter.hp
        return result
