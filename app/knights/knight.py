class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            protection: int
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def __sub__(self, other: "Knight") -> int:
        result = self.hp - other.power + self.protection
        return 0 if result < 0 else result
