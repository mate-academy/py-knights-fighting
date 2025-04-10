class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name

        for key, value in effect.items():
            setattr(self, key, value)
