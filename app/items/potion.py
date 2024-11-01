from app.items.potion_effect import Effect


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        try:
            self.effect = Effect(effect["hp"], effect["power"], effect["protection"])
        except KeyError:
            self.effect = Effect(effect["hp"], effect["power"])

    # def __getitem__(self, key):
    #     if key == "name":
    #         print(self.name)
    #         return self.name
    #     elif key == "effect":
    #         print(self.effect)
    #         return self.effect
    #     else:
    #         raise KeyError(f"Key {key} not found in Potion")