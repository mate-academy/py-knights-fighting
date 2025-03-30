class Battle:
    def __init__(self, knight1: dict, knight2: dict) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def execute(self) -> None:
        damage1 = self.knight1.get_damage(self.knight2.protection)
        damage2 = self.knight2.get_damage(self.knight1.protection)

        self.knight1.take_damage(damage2)
        self.knight2.take_damage(damage1)

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
