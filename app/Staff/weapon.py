class Weapon:
    def __init__(
            self,
            name: str,
            power: int = 0
    ) -> None:
        self.name = name
        self.power = power
