class Effect:
    def __init__(self, effect_cfg: dict) -> None:
        self.hp = effect_cfg.get("hp", 0)
        self.power = effect_cfg.get("power", 0)
        self.protection = effect_cfg.get("protection", 0)
