class Armor:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return f"{self.part} with {self.protection} protection"


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> str:
        return f"{self.name} with {self.power} power"


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def __repr__(self) -> str:
        return f"{self.name} potion"
