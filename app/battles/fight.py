from app.preparations.knight_stats import Knight


class Fight:

    @staticmethod
    def battle(first_opponent: Knight, second_opponent: Knight) -> None:

        first_opponent.health -= (second_opponent.power
                                  - first_opponent.protection)

        if first_opponent.health < 0:
            first_opponent.health = 0

        second_opponent.health -= (first_opponent.power
                                   - second_opponent.protection)

        if second_opponent.health < 0:
            second_opponent.health = 0
