class Armour:
    def __init__(self, name: str, points: int) -> None:
        self.name = name
        self.points = points


class Weapon:
    def __init__(self, name: str, points: int) -> None:
        self.name = name
        self.points = points


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect
