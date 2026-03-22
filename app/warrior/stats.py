class Stats:
    def __init__(
            self, hp: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    def __add__(self, other: Stats) -> Stats:
        return Stats(
            self.hp + other.hp,
            self.power + other.power,
            self.protection + other.protection
        )

    def __sub__(self, other: Stats) -> Stats:
        return Stats(
            self.hp - (other.power - self.protection),
            self.power,
            self.protection
        )
