class Potion:
    def __init__(self, potion: dict) -> None:
        if potion and potion["effect"]:
            self.name = potion["name"]
            self.effect = potion["effect"]
