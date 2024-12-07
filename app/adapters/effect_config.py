class EffectConfig:
    def __init__(self, effect_dict: dict[str, str | int | dict]) -> None:
        self.power, self.protection, self.hp = 0, 0, 0

        if effect_dict.get("power"):
            self.power = effect_dict.get("power")
        elif effect_dict.get("protection"):
            self.protection = effect_dict.get("protection")
        elif effect_dict.get("effect"):
            self._extract_effect(effect_dict.get("effect"))

    def _extract_effect(self, config: dict[str, int]) -> None:
        if config is not None:
            self.power = config.get("power", 0)
            self.protection = config.get("protection", 0)
            self.hp = config.get("hp", 0)
