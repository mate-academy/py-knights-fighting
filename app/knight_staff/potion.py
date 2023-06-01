
class Effect:
    def __init__(self,
                 power: int = None,
                 hp: int = None,
                 protection: int = None) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = self.get_effect(effect)

    @staticmethod
    def get_effect(effect: dict) -> Effect:
        power = None
        hp = None
        protection = None
        if effect.get("power"):
            power = effect.get("power")
        if effect.get("hp"):
            hp = effect.get("hp")
        if effect.get("protection"):
            protection = effect.get("protection")

        return Effect(power, hp, protection)
