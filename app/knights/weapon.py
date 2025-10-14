from typing import Dict

class Weapon:
    def __init__(self, data: Dict):
        self.name: str = data.get("name", "")
        self.power: int = int(data.get("power", 0))