from app.peoples.knights import Knight


class Battle:

    @staticmethod
    def fight(knight1: "Knight", knight2: "Knight") -> None:
        knight1.take_damage(knight2.power)
        knight2.take_damage(knight1.power)
