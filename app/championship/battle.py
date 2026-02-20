from app.championship.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        # 2 knight
        self.knight1 = knight1
        self.knight2 = knight2

    @staticmethod
    def hp_check(knight: Knight) -> None:
        if knight.hp <= 0:
            knight.hp = 0

    def fight(self) -> dict[str, int]:
        self.attack(self.knight1, self.knight2)
        self.attack(self.knight2, self.knight1)
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp
        }

    @staticmethod
    def attack(attacker: Knight, defender: Knight) -> None:
        damage = attacker.power - defender.protection
        defender.hp -= damage
        Battle.hp_check(defender)
