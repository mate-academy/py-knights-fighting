from app.characters.knight import Knight


class Battle:
    fighters = []

    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight
        self.knights = [self.first_knight, self.second_knight]
        Battle.fighters.extend(self.knights)

    def fight(self) -> None:
        self.first_knight.hit(self.second_knight)
        self.second_knight.hit(self.first_knight)
        self.check_for_hp(self.knights)

    @staticmethod
    def check_for_hp(knights: list[Knight]) -> None:
        for knight in knights:
            if knight.hp <= 0:
                knight.hp = 0

    @classmethod
    def get_result(cls) -> dict:
        result = {}
        for fighter in cls.fighters:
            result[fighter.name] = fighter.hp
        return result
