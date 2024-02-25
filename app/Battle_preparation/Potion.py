class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = potion["name"]
        self.effect = potion["effect"]

    def potion_effect(self, knight: dict) -> None:
        for effect_name, effect_value in self.effect.items():
            setattr(knight, effect_name,
                    getattr(knight, effect_name) + effect_value)
