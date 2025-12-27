class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def get_effect(self, effest: str) -> int:
        return self.effect.get(effest, 0)
