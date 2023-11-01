from characters.knights import Knights


class Fight:
    def __init__(self, stats: dict) -> None:
        super().__init__(stats)

    @staticmethod
    def fight(warrior: Knights, opponent_name: str) -> None:
        for opponent in Knights.list_of_heroes:
            if opponent.name == opponent_name:
                warrior.hp -= opponent.power - warrior.protection
                opponent.hp -= warrior.power - opponent.protection

                for hero in [warrior, opponent]:
                    if hero.hp <= 0:
                        hero.hp = 0
