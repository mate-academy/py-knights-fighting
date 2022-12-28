class Potion:
    def __init__(self, potion_dict: dict) -> None:
        self.name = potion_dict["name"]
        self.hp = potion_dict["effect"].get("hp", 0)
        self.power = potion_dict["effect"].get("power", 0)
        self.protection = potion_dict["effect"].get("protection", 0)
