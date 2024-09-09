from app.knights.class_knight import Knight


class Battle:
    def __init__(self, attacker: Knight, defender: Knight) -> None:
        self.attacker = attacker
        self.defender = defender

    def battle_round(self) -> None:
        # Calculate the damage for each knight
        self.defender.hp -= max(self.attacker.total_power
                                - self.defender.total_protection, 0)
        self.attacker.hp -= max(self.defender.total_power
                                - self.attacker.total_protection, 0)

        self.defender.total_hp -= self.attacker.total_power
        self.attacker.total_hp -= self.defender.total_power

        # We check if someone died in the battle
        self.defender.hp = max(self.defender.hp, 0)
        self.defender.total_hp = max(self.defender.total_hp, 0)

        self.attacker.hp = max(self.attacker.hp, 0)
        self.attacker.total_hp = max(self.attacker.total_hp, 0)
