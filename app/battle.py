from app.knights import Knight


class Battle:

    def __init__(self, knight1: Knight, knight2: Knight):
        self.knight1 = knight1
        self.knight2 = knight2

    def calculate_damage(self, attacker: Knight, defender: Knight) -> int:
        return max(0, attacker.power - defender.protection)

    def fight(self) -> dict:
        damage_to_knight1 = self.calculate_damage(self.knight2, self.knight1)
        damage_to_knight2 = self.calculate_damage(self.knight1, self.knight2)

        self.knight1.take_damage(damage_to_knight1)
        self.knight2.take_damage(damage_to_knight2)

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
