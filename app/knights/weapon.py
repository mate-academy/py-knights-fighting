class Weapon:
    def __init__(self, name: str, power: str) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> None:
        return f"{self.name} (+{self.power} Power)"
