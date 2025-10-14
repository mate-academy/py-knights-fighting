from typing import Dict


class Weapon:
    def __init__(self, data: Dict) -> None:
        self.name = data.get("name", "Fists")
        self.power = data.get("power", 0)
