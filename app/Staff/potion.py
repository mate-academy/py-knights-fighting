class Potion:
    def __init__(
            self,
            name: str,
            power: int = 0,
            health: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.protection = protection
