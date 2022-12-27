from __future__ import annotations


class Potion:
    def __init__(self, name: str = None, effect: dict = None) -> None:
        if effect is None:
            effect = {"power": 0, "hp": 0, "protection": 0}
        self.name = name
        self.effect = effect

    @staticmethod
    def parse_potion(potion_value: dict) -> Potion:
        if potion_value is None:
            return Potion()
        return Potion(potion_value.get("name", None),
                      potion_value.get("effect",
                                       {"power": 0, "hp": 0, "protection": 0}))

    def get_effect_on_power(self) -> int:
        return self.effect.get("power", 0)

    def get_effect_on_hp(self) -> int:
        return self.effect.get("hp", 0)

    def get_effect_on_protection(self) -> int:
        return self.effect.get("protection", 0)
