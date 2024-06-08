class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = potion["name"]
        self.effect = potion["effect"]
