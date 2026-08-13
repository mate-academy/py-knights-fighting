from app.knight import Knight


class Battle:

    def __init__(self) -> None:
        self.knights = {}
        self.results = {}

    def call_the_knight(self, knights: dict) -> None:
        self.knights = {
            knight["name"]: Knight(**knight)
            for knight in knights.values()
        }

    def prepare(self) -> None:
        for name, knight in self.knights.items():
            knight.preparation()

    def battle(self, fights: list) -> None:
        for fighters in fights:
            self.fight(*fighters.split(" vs "))

        self.after_battle()

    def fight(self, first_knight: str, second_knight: str) -> None:
        self.knights[first_knight].hp -= (
            self.knights[second_knight].power
            - self.knights[first_knight].protection
        )
        self.knights[second_knight].hp -= (
            self.knights[first_knight].power
            - self.knights[second_knight].protection
        )

        if self.knights[first_knight].hp <= 0:
            self.knights[first_knight].hp = 0
        if self.knights[second_knight].hp <= 0:
            self.knights[second_knight].hp = 0

    def print_results(self) -> dict:
        return self.results

    def after_battle(self) -> None:
        for knight in self.knights.values():
            self.results[knight.name] = knight.hp
