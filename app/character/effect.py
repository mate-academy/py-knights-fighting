from dataclasses import dataclass


@dataclass
class Effect:
    power: int | None
    hp: int | None
    protection: int | None

    def get_effect_value(self, effect: str) -> int:
        try:
            value = getattr(self, effect) or 0
            return value
        except AttributeError:
            print(f"AttributeError: {effect} does not exist.")
            return 0
