class Potion:
    potions = {}

    def __init__(self, potion: dict, owner: str) -> None:
        self.owner = owner
        for key, value in potion["effect"].items():
            setattr(self, key, value)

        Potion.potions[potion["name"]] = self
