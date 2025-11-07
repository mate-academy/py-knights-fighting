class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def __str__(self) -> str:
        return f"Potion is {self.name}"
