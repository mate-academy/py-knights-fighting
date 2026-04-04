from app.knights import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def run(self) -> dict:
        self.knight1.get_damage(self.knight2.current_power)
        self.knight2.get_damage(self.knight1.current_power)

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp
        }
