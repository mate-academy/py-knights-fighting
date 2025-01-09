from app.entities.behavior import EffectOnHp, EffectOnProtection, EffectOnPower
from app.outfit.potion.effect import Effect


class Potion(EffectOnHp, EffectOnProtection, EffectOnPower):
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect
