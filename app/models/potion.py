class Potion:
    def __init__(self, name: str, effect: dict[str, int]) -> None:
        self.name: str = name
        self.effect: dict[str, int] = effect

    def __repr__(self) -> str:
        return f"Potion(name={self.name}, effect={self.effect})"
