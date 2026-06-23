from app.knight import Knight


class Battle:

    def __init__(self, left_knight: Knight, right_knight: Knight) -> None:
        self.left_knight = left_knight
        self.right_knight = right_knight

    def duel(self) -> None:
        left_damage = (
            self.right_knight.power - self.left_knight.protection
        )
        right_damage = (
            self.left_knight.power - self.right_knight.protection
        )

        self.left_knight.hp = max(0, self.left_knight.hp - left_damage)
        self.right_knight.hp = max(0, self.right_knight.hp - right_damage)
