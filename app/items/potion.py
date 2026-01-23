from app.items.potion_effect import Effect


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        try:
            self.effect = Effect(effect["hp"],
                                 effect["power"], effect["protection"])
        except KeyError:
            self.effect = Effect(effect["hp"], effect["power"])
