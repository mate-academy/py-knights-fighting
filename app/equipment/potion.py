class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = None
        self.effect = None
        if potion is not None:
            for key in potion:
                setattr(self, key, potion[key])
