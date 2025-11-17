class Potion:
    def __init__(self, name: str, effects: dict) -> None:
        self.name = name
        self.effects = effects

berserk_potion = Potion("Berserk", {"power": 15, "hp": -5, "protection": 10})