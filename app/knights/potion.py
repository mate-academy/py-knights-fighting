class Potion:
    def __init__(self, effect: dict) -> None:
        self.effect = effect

    def apply(self, knight: object) -> None:
        for stat, value in self.effect.items():
            setattr(knight, stat, getattr(knight, stat) + value)
