from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def get_instance(cls, potion: dict) -> None | Potion:
        if potion:
            return cls(**potion)

    def if_effect_exist_return_value(self, effect_name: str) -> int:
        if effect_name in self.effect:
            return self.effect[effect_name]

        return 0
