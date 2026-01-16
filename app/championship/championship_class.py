from app.knight.knight_class import Knight


class Championship:
    """
    Organize fighting championship between Knights.
    """
    def __init__(self) -> None:
        self.results = {}

    def fight(self, *knights: tuple[Knight, Knight]) -> None:
        """
        Carry out a battle between two Knight instances and fix the results.
        :param knights:
        """
        for index in range(len(knights)):
            knights[index].hp -= (knights[(index + 1) % 2].power
                                  - knights[index].protection)
            if knights[index].hp <= 0:
                knights[index].hp = 0
            self.results[knights[index].name] = knights[index].hp

    def get_championship_results(self) -> dict:
        return self.results
