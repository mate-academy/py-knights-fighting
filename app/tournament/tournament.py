from app.characters.knight import Knight


class Tournament:
    def __init__(self, pairs: list[tuple[Knight, Knight]]) -> None:
        self.pairs = pairs

    def fight(self, knight1: Knight, knight2: Knight) -> None:
        # no fighting when someone is dead
        if knight1.hp and knight2.hp:
            knight1.attack(knight2)
            knight2.attack(knight1)

    def battle(self) -> dict:
        for pair in self.pairs:
            self.fight(*pair)

        return {
            knight.name: knight.hp
            for pair in self.pairs
            for knight in pair
        }
