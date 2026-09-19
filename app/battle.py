from app.knight_clas import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def prepare(self) -> None:
        self.knight1.before_fight()
        self.knight2.before_fight()

    def fight(self) -> None:
        combatants = [
            (self.knight1, self.knight2.power),
            (self.knight2, self.knight1.power),
        ]

        for defender, attacker_power in combatants:
            damage = attacker_power - defender.protection
            if damage > 0:
                defender.hp = max(0, defender.hp - damage)

    def start(self) -> None:
        self.prepare()
        self.fight()
