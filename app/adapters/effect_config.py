from typing import cast


class EffectConfig:
    def __init__(
        self, effect_dict: dict[str, int | str | dict[str, int | str]]
    ) -> None:
        self.power: int = 0
        self.protection: int = 0
        self.hp: int = 0

        if effect_dict.get("power"):
            self.power = int(str(effect_dict.get("power", 0)))
        elif effect_dict.get("protection"):
            self.protection = int(str(effect_dict.get("protection", 0)))
        elif effect_dict.get("effect"):
            self._extract_effect(cast(dict[str, int], effect_dict.get("effect", 0)))

    def _extract_effect(self, config: dict[str, int]) -> None:
        self.power = config.get("power", 0)
        self.protection = config.get("protection", 0)
        self.hp = config.get("hp", 0)
