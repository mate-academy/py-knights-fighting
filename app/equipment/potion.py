class Potion:
    def __init__(self, potion_cfg: dict) -> None:
        self.name = potion_cfg["name"]
        self.hp = potion_cfg["effect"].get("hp", 0)
        self.power = potion_cfg["effect"].get("power", 0)
        self.protection = potion_cfg["effect"].get("protection", 0)
