from characters.knights import Knights


class Fight:
    def __init__(self) -> None:
        pass

    @staticmethod
    def fight(warrior: Knights, opponent: Knights) -> None:

        warrior.hp -= opponent.power - warrior.protection
        opponent.hp -= warrior.power - opponent.protection

        for hero in [warrior, opponent]:
            if hero.hp <= 0:
                hero.hp = 0
