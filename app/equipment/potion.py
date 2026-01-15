class Effect:
    def __init__(self, attr: str, power: int) -> None:
        self.attr = attr
        self.power = power


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effects = []

        for effect_attr, effect_power in effect.items():
            self.effects.append(Effect(effect_attr, effect_power))
