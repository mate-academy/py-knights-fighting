class Effect:
    def __init__(self, potion_effect: dict) -> None:
        self.power = potion_effect.get("power", 0)
        self.hp = potion_effect.get("hp", 0)
        self.protection = potion_effect.get("protection", 0)


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect
