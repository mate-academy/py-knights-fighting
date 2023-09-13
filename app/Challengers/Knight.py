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
        if value < 0:
            self._hp = 0
        else:
            self._hp = value
