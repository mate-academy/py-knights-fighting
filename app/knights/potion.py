from app.knights.potion_effect import PotionEffect


class Potion:
    def __init__(self, name: str, effect: PotionEffect) -> None:
        self.name = name
        self.effect = effect
