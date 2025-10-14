from typing import Dict

class Armour:
    def __init__(self, data: Dict):
        self.part: str = data.get("part", "")
        self.protection: int = int(data.get("protection", 0))
