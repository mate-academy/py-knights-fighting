from app.knights import Knight


class Battle:
    @staticmethod
    def calculate_damage(attacker: Knight, defender: Knight) -> None:
        """Calculate the damage dealt and return the updated hp
        for both knights."""
        damage_to_defender = max(0, attacker.power - defender.protection)
        damage_to_attacker = max(0, defender.power - attacker.protection)

        # Apply damage for both knights
        defender.receive_damage(damage_to_defender)
        attacker.receive_damage(damage_to_attacker)

    def fight(self, knight1: Knight, knight2: Knight) -> dict:
        """Simulate a fight between two knights and return the results."""
        self.calculate_damage(knight1, knight2)
        return {knight1.name: knight1.hp, knight2.name: knight2.hp}
