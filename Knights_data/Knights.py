from Knights_data.Stats import KnightStats


class Knight:
    def __init__(self, knight: KnightStats) -> None:
        self.hp = knight.hp
        self.power = knight.power
        self.protection = knight.protection

    def __sub__(self, other) -> None:
        self.hp -= other.power - self.protection
        if self.hp < 0:
            self.hp = 0
        other.hp -= self.power - other.protection
        if other.hp < 0:
            other.hp = 0

    def __repr__(self):
        return f"hp: {self.hp}, power: {self.power}, protection: {self.protection}\n"
