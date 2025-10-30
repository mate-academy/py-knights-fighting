
class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class ArmourPart:
    def __init__(self, parts: str, protection: int) -> None:
        self.parts = parts
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect
