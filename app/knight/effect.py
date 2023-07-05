class Effect:
    def __init__(
            self,
            power: int = None,
            hp: int = None,
            protection: int = None
    ) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection
