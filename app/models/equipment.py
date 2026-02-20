class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f"{self.name} (Power: {self.power})"


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __str__(self) -> str:
        return f"{self.part} (Protection: {self.protection})"


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def __str__(self) -> str:
        return f"{self.name} (Effect: {self.effect})"
