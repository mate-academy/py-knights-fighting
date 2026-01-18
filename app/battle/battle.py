from app.models.knight import Knight


class Battle:

    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> dict:
        knight1_hp = self.knight1.hp
        knight2_hp = self.knight2.hp
        power_knight1 = self.knight1.total_power
        power_knight2 = self.knight2.total_power
        protection_knight1 = self.knight1.total_protection
        protection_knight2 = self.knight2.total_protection
        if protection_knight1 < power_knight2:
            knight1_hp -= (power_knight2 - protection_knight1)
            if knight1_hp <= 0:
                knight1_hp = 0
        if protection_knight2 < power_knight1:
            knight2_hp -= (power_knight1 - protection_knight2)
            if knight2_hp <= 0:
                knight2_hp = 0
        battle_result = {
            self.knight1.name: knight1_hp,
            self.knight2.name: knight2_hp
        }
        return battle_result
