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
        first = self.knights[first_knight]
        second = self.knights[second_knight]

        first_damage = calculate_damage(second.power, first.protection)
        second_damage = calculate_damage(first.power, second.protection)

        first.hp -= first_damage
        second.hp -= second_damage

        if first.hp <= 0:
            first.hp = 0
        if second.hp <= 0:
            second.hp = 0

    def print_results(self) -> dict:
        return self.results

    def after_battle(self) -> None:
        for knight in self.knights.values():
            self.results[knight.name] = knight.hp


def calculate_damage(power: int, protection: int) -> int:
    return max(0, power - protection)
