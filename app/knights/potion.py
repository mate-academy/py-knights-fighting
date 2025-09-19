class Potion:
    def __init__(self, name: str, effect: dict):
        self.name = name
        self.effect = effect  # {"hp": +10, "power": +5, "protection": -3}
