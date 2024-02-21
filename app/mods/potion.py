class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


def get_potion(potion: dict) -> Potion:
    return Potion(
        potion["name"],
        potion["effect"]
    )
