from app.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def conduct_battle(self) -> None:
        self.knight1.take_damage(self.knight2.power)
        self.knight2.take_damage(self.knight1.power)

        if self.knight1.is_defeated():
            self.knight1.hp = 0
        if self.knight2.is_defeated():
            self.knight2.hp = 0

    def get_result(self) -> dict:
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
