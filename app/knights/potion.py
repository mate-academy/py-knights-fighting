class Potion:
    def __init__(self, name: str, effect: str) -> None:
        self.name = name
        self.effect = effect

    def __str__(self) -> None:
        return f"{self.name} ({self.effect})"
