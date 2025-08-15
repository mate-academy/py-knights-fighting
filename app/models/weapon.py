class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name: str = name
        self.power: int = power

    def __repr__(self) -> str:
        return f"Weapon(name='{self.name}', power={self.power})"
