from app.equipment.effect import Effect


class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = potion["name"]
        self.effect = Effect(potion["effect"])
