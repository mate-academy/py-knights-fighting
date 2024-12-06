from app.adapters.effect_adapter import EffectAdapter


class Effect:
    def __init__(self, effect_data: EffectAdapter):
        self.power = effect_data.power
        self.protection = effect_data.protection
        self.hp = effect_data.hp

    def get_power(self):
        return self.power

    def get_protection(self):
        return self.protection

    def get_hp(self):
        return self.hp