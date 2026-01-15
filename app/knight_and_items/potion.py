class Potion:

    def __init__(self, stats: dict) -> None:
        self.name = stats.get("name")

        self.hp = 0
        self.power = 0
        self.protection = 0

        self.apply_effects(stats.get("effect"))

    def apply_effects(self, effects: dict) -> None:
        for effect in effects:
            effects_value = effects.get(effect)
            if effects_value is not None:
                setattr(self, effect, effects_value)
