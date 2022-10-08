class Potion:
    def __init__(self,
                 name: str = "Unknown",
                 effect: dict = None) -> None:
        if effect is None:
            effect = {}
        self.name = name
        self.effect = effect
