from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def get_instance(cls, potion: dict) -> None | Potion:
        return cls(**potion) if potion else None

    def if_effect_exist_return_value(self, effect_name: str) -> int:
        return self.effect.get(effect_name, 0)
