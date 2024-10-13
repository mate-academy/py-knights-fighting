class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def __repr__(self) -> str:
        return f"Potion(name={self.name}, effect={self.effect})"
