class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f"(name: {self.name}, power: {self.power})"
