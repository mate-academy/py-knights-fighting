class Potion:

    def __init__(self, name: str, effects: dict) -> None:
        self.name = name
        self.effects = dict(hp=0, power=0, protection=0)
        for key, value in effects.items():
            self.effects[key] = value
