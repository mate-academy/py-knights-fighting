class Effect:
    def __init__(self, hp: int, power: int, protection: int = 0) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection
