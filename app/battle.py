from app.knights import Knight


class Battle:
    def __init__(self, knight_a: Knight, knight_b: Knight) -> None:
        self.knight_a = knight_a
        self.knight_b = knight_b

    def fight(self) -> dict[str, int]:
        damage_to_a = max(0, self.knight_b.power - self.knight_a.protection)
        damage_to_b = max(0, self.knight_a.power - self.knight_b.protection)

        self.knight_a.receive_damage(damage_to_a)
        self.knight_b.receive_damage(damage_to_b)

        return {
            self.knight_a.name: self.knight_a.hp,
            self.knight_b.name: self.knight_b.hp,
        }
