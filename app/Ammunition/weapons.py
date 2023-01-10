class Weapon:

    weapons = {}

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
        self.__class__.weapons[self.name] = self
