class PotionEffect:
    def __init__(self,
                 power: int = 0,
                 hp: int = 0,
                 protection: int = 0
                 ) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection
