class Potion:
    def __init__(self, potion: dict | None) -> None:
        self.effect = potion["effect"] if potion else {}

    def get_effect(self, attribute: str) -> int:
        return self.effect.get(attribute, 0)
