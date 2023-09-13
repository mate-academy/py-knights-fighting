class Hero:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: int = 0) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value if value >= 0 else 0
