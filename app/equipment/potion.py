class Potion:
    def __init__(self, name: str, potion_info: dict) -> None:
        self.name = name
        self.power = potion_info.get("power", 0)
        self.protection = potion_info.get("protection", 0)
        self.hp = potion_info.get("hp", 0)
