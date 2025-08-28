class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def print_stats(self) -> None:
        print(f'Using armor: {self.part}, protection: {self.protection}.')
