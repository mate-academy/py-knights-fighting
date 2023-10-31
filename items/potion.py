class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def __str__(self) -> str:
        return f"(name: {self.name}, effect: {self.effect})"

    @staticmethod
    def crate_potion(knight: dict) -> "Potion":
        potion = knight["potion"]
        if potion:
            return Potion(**potion)
