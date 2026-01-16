class Armour:
    def __init__(self, part: str = None, protection: int = None) -> None:
        self.part = part if part is not None else "Unknown Part"
        self.protection = protection if protection is not None else 0


class Potion:
    def __init__(self, name: str = None, effect: dict = {}) -> None:
        self.name = name
        self.effect = effect


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
