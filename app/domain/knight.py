class Knight:
    def __init__(
        self, name: str, hp: int, power: int, protection: int
    ) -> None:
        self.name = name
        self._hp = hp
        self.power = power
        self.protection = protection

    def __repr__(self) -> str:
        return (
            f"Knight(name={self.name}, hp={self.hp}, "
            f"power={self.power}, protection={self.protection})"
        )

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        if value >= 0:
            self._hp = value
        else:
            self._hp = 0
