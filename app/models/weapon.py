class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __repr__(self) -> None:
        return f"Weapon({self.name}, Power: {self.power})"
