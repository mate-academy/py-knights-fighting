class Potion:
    def __init__(self, potion_data: dict) -> None:
        self.name = potion_data["name"]
        self.power = potion_data["effect"].get("power", 0)
        self.hp = potion_data["effect"].get("hp", 0)
        self.protection = potion_data["effect"].get("protection", 0)
