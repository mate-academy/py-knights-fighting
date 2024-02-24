from app.types.effect import Effect


class Potion:
    def __init__(self, name: str, effect: Effect):
        self.name = name
        self.effect = effect
