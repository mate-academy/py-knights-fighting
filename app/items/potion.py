from app.items.potion_effect import Effect


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = Effect(effect["hp"], effect["power"])
