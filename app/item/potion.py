class PotionEffect:
    def __init__(self, hp: int, power: int, protection: int) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: PotionEffect) -> None:
        self.name = name
        self.effect = effect
