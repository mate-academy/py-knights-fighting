class Potion:
    def __init__(self, potion: dict) -> None:
        if potion is not None:
            self.name = potion["name"]
            for key, value in potion["effect"].items():
                setattr(self, key, value)
