from app.models.knight import Knight


class Arena:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def battle(self) -> None:
        """
        Executes a single round of battle between the two knights.
        Ensures damage cannot heal a knight and health points cannot drop < 0.
        """
        # Calculate damage dealt simultaneously
        damage_to_k1 = max(self.knight_2.power - self.knight_1.protection, 0)
        damage_to_k2 = max(self.knight_1.power - self.knight_2.protection, 0)

        # Apply damage and enforce the 0 HP floor constraint
        self.knight_1.hp = max(self.knight_1.hp - damage_to_k1, 0)
        self.knight_2.hp = max(self.knight_2.hp - damage_to_k2, 0)
