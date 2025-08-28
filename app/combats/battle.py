from app.knights.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def start_battle(self) -> dict:
        print(f'The battle between {self.knight1} vs {self.knight2} started.')
        self.knight1.print_stats()
        self.knight2.print_stats()

        knight1_hp = self.knight1.total_hp()
        knight2_hp = self.knight2.total_hp()

        knight1_hp -= self.knight2.total_power() - self.knight1.protection()
        knight2_hp -= self.knight1.total_power() - self.knight2.protection()

        if knight1_hp <= 0:
            knight1_hp = 0

        if knight2_hp <= 0:
            knight2_hp = 0

        print(f'The battle result is {self.knight1.name}: '
              f' {knight1_hp}, {self.knight2.name}: {knight2_hp}')
        return {
            self.knight1.name: knight1_hp,
            self.knight2.name: knight2_hp,
        }
