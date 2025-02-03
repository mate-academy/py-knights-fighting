from app.items.potion_effect import PotionEffect


class Potion:
    def __init__(self, name: str, effects: list[PotionEffect]) -> None:
        self.name = name
        self.effects = effects
