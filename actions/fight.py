from characters.knight import Knight


class Fight:

    @staticmethod
    def fight(warrior: Knight, opponent: Knight) -> None:

        warrior.hp -= opponent.power - warrior.protection
        opponent.hp -= warrior.power - opponent.protection

        for hero in [warrior, opponent]:
            if hero.hp <= 0:
                hero.hp = 0
