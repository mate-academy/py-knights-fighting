from typing import List, Dict


class Armour:
    def __init__(self, data: List[Dict]) -> None:
        self.parts = data

    def get_total_protection(self) -> int:
        return sum(part.get("protection", 0) for part in self.parts)
