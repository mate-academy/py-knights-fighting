class Knight:
    knights = {}

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        Knight.knights[self.name] = self
