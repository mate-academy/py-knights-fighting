class Potion:
    def __init__(self,
                 name: str,
                 protection: int = 0,
                 hp: int = 0,
                 power: int = 0
                 ) -> None:
        self.name = name
        self.protection = protection
        self.hp = hp
        self.power = power
