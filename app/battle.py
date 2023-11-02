from app.knight.knight import Knight


class Battle:
    @classmethod
    def fight(cls, knight1: Knight, knight2: Knight) -> None:
        knight1.hp = cls.calculate_damage(
            knight1.total_hp(),
            knight2.total_power(),
            knight1.total_protection()
        )
        knight2.hp = cls.calculate_damage(
            knight2.total_hp(),
            knight1.total_power(),
            knight2.total_protection()
        )

    @staticmethod
    def calculate_damage(
            health_points: int, attacker_power: int, defender_protection: int
    ) -> int:
        damage = health_points - (attacker_power - defender_protection)

        # check if someone fell in battle
        if damage <= 0:
            return 0

        return damage
