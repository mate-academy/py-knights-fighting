class Potion:

    def __init__(self, effect_hp: int = 0,
                 effect_power: int = 0,
                 effect_protection: int = 0
                 ) -> None:
        self.effect_hp = effect_hp
        self.effect_power = effect_power
        self.effect_protection = effect_protection
