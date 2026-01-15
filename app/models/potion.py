from app.models.effect import Effect


class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = potion.get("name")
        self.effect = Effect(potion.get("effect"))
