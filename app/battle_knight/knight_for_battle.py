class KnightForBattle:
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

    def battle_knight(self, other: KnightForBattle) -> None:
        self.hp -= other.power - self.protection
        self.hp = 0 if self.hp <= 0 else self.hp
