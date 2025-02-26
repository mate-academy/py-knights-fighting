from app.koc.knight import Knight


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        from app.koc.effect import Effect

        self.name = name
        self.effect = Effect(**effect)

    def apply(self, knight: Knight) -> None:
        self.effect.apply(knight)
