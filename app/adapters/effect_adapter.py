class EffectAdapter:
    def __init__(self, config: dict):
        self.power, self.protection, self.hp = 0, 0, 0
        if config.get("power"):
            self.power = config.get("power", 0)
        elif config.get("protection"):
            self.protection = config.get("protection", 0)
        elif config.get("effect"):
            self._extract_effect(config.get("effect"))

    def _extract_effect(self, config):
        if config is not None:
            self.power = config.get("power", 0)
            self.protection = config.get("protection", 0)
            self.hp = config.get("hp", 0)
