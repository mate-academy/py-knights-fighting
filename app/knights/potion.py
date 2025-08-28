class Potion:
    power: int = 0
    hp: int = 0
    protection: int = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def print_stats(self) -> None:
        print(
            f'Using potion: {self.name}\n'
            f'\t - power: {self.power}\n'
            f'\t - hp: {self.hp}\n'
            f'\t - protection: {self.protection}')

    def prepare(self, power: int, hp: int, protection: int) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection
