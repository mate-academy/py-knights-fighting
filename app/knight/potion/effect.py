from __future__ import annotations


class PotionEffect:
    def __init__(
            self,
            hp: int,
            power: int,
            protection: int
    ) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    @classmethod
    def get_from_dict(cls, potion_effect_dict: dict[str, int]) -> PotionEffect:
        return cls(
            hp=potion_effect_dict.get("hp", 0),
            power=potion_effect_dict.get("power", 0),
            protection=potion_effect_dict.get("protection", 0)
        )
