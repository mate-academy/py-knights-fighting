class Potion:
    def __init__(
            self, part: str,
            hp: int = 0,
            power: int = 0,
            protection: int = 0,
    ) -> None:
        self.part = part
        self.hp = hp
        self.power = power
        self.protection = protection
