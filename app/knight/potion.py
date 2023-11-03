class Potion:
    def __init__(
            self, name: str,
            hp: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
