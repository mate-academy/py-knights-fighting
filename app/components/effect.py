class Effect:
    def __init__(self, hp: int = 0, power: int = 0,
                 protection: int = 0) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    def __repr__(self) -> str:
        return str(self.__dict__)
