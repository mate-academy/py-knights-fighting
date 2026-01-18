from app.models.knight import Knight


class Battle:

    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def _apply_damage(self, attacker: Knight, defender: Knight) -> None:
        damage = attacker.total_power - defender.total_protection
        if damage > 0:
            defender.hp = max(defender.hp - damage, 0)

    def fight(self) -> dict:
        self._apply_damage(self.knight1, self.knight2)
        self._apply_damage(self.knight2, self.knight1)
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
