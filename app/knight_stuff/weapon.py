class Weapon:

    def __init__(self, name: str, power: int = 0) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> None:
        print(f"Weapon {self.name} has {self.power} power")
