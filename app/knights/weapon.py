class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def print_stats(self) -> None:
        print(f'Using weapon: {self.name}, power: {self.power}.')
