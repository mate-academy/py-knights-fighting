class Weapon:
    def __init__(self, name: str, power: int) -> None:
        if power < 0:
            raise ValueError("Weapon power cannot be negative.")

        self.__name: str = name
        self.__power: int = power

    @property
    def name(self) -> str:
        return self.__name

    @property
    def power(self) -> int:
        return self.__power

    def __repr__(self) -> str:
        return f"Weapon(name='{self.name}', power={self.power})"
