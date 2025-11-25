from __future__ import annotations


class Effect:
    def __init__(self, power: int = None,
                 hp: int = None,
                 protection: int = None) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def init_from_dict(cls, effect_dict: dict) -> Effect:
        power = effect_dict["power"] if "power" in effect_dict else None
        hp = effect_dict["hp"] if "hp" in effect_dict else None
        protection = effect_dict["protection"]\
            if "protection" in effect_dict else None
        return cls(power=power, hp=hp, protection=protection)
