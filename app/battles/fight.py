from app.preparations.knight_stats import Knight


class Fight:

    @staticmethod
    def battle(first_opponent: Knight, second_opponent: Knight) -> None:

        first_opponent.hp -= (
            second_opponent.power - first_opponent.protection
        )

        Fight.no_negative_health(first_opponent)

        second_opponent.hp -= (
            first_opponent.power - second_opponent.protection
        )

        Fight.no_negative_health(second_opponent)

    @staticmethod
    def no_negative_health(participant: Knight) -> None:
        if participant.hp < 0:
            participant.hp = 0
