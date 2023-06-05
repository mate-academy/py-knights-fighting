
class Effect:
    def __init__(self,
                 power: int = None,
                 hp: int = None,
                 protection: int = None) -> None:
        if power:
            self.power = power
        if hp:
            self.hp = hp
        if protection:
            self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = self.get_effect(effect)

    @staticmethod
    def get_effect(effect: dict) -> Effect:
        return Effect(effect.get("power"),
                      effect.get("hp"),
                      effect.get("protection"))
