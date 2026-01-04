from app.knight import Knight


class Battle:

    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def battle(self) -> None:
        self.knight_1.prepare_to_battle()
        self.knight_2.prepare_to_battle()
        self.knight_1.hp = self.fight(
            self.knight_1.hp,
            self.knight_2.power,
            self.knight_1.protection
        )
        self.knight_2.hp = self.fight(
            self.knight_2.hp,
            self.knight_1.power,
            self.knight_2.protection
        )

    @staticmethod
    def fight(hp: int, power: int, protection: int) -> int:
        hp -= power - protection
        return hp if hp >= 0 else 0
