from app.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def conduct_battle(self) -> None:
        self.knight1.adjust_hp(self.knight2.total_power)
        self.knight2.adjust_hp(self.knight1.total_power)

    def get_result(self) -> dict:
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
