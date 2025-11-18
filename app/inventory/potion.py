class PotionEffect:
    def __init__(self, power: int, hp: int, protection: int) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        power = effect.get("power", 0)
        hp = effect.get("hp", 0)
        protection = effect.get("protection", 0)

        self.name = name
        self.effect = PotionEffect(power, hp, protection)
