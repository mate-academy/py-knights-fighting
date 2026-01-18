from app.entities.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def start(self) -> dict:
        if self.knight1.potion and not self.knight1.potion_used:
            self.knight1.potion.apply(self.knight1)
            self.knight1.potion_used = True

        if self.knight2.potion and not self.knight2.potion_used:
            self.knight2.potion.apply(self.knight2)
            self.knight2.potion_used = True

        while self.knight1.is_alive() and self.knight2.is_alive():
            self.knight1.attack(self.knight2)
            if not self.knight2.is_alive():
                break

            self.knight2.attack(self.knight1)

        return {
            self.knight1.name: max(self.knight1.hp, 0),
            self.knight2.name: max(self.knight2.hp, 0),
        }
