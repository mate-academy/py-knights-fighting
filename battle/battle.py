from knights.knight import Knight


class Battle:
    def __init__(self) -> None:
        pass

    def knight_battle(self, opponent1: Knight, opponent2: Knight) -> None:
        opponent1.hp -= opponent2.power - opponent1.knight_protection
        opponent2.hp -= opponent1.power - opponent2.knight_protection

        if self.knight_is_fell(opponent1):
            opponent1.hp = 0
        if self.knight_is_fell(opponent2):
            opponent2.hp = 0

    @staticmethod
    def knight_is_fell(knight: Knight) -> bool:
        return True if knight.hp <= 0 else False
