from .effect import Effect


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect
