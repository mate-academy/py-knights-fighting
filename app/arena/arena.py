from app.models.knights import Knight


class Arena:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> dict[str, dict[str, int] | int]:

        damage1 = self.knight1.attack(self.knight2)
        damage2 = self.knight2.attack(self.knight1)
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
            "damage_dealt": {
                self.knight1.name: damage1,
                self.knight2.name: damage2
            }
        }
