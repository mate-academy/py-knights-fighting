class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self._name = name
        self._power = power

    @property
    def name(self) -> str:
        return self._name

    @property
    def power(self) -> int:
        return self._power
