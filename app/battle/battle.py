from app.entities.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def start(self) -> None:
        if self.knight1.potion:
            self.knight1.potion.apply(self.knight1)

        if self.knight2.potion:
            self.knight2.potion.apply(self.knight2)

        damage_to_2 = max(
            0,
            self.knight1.power - self.knight2.protection
        )
        damage_to_1 = max(
            0,
            self.knight2.power - self.knight1.protection
        )

        self.knight2.hp -= damage_to_2
        self.knight1.hp -= damage_to_1
