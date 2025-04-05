from typing import Dict


class Armour:
    def __init__(
            self,
            parts: list[Dict] = None
    ) -> None:
        self.parts = parts

    def total_protection(self) -> int:
        return sum(part.get("protection", 0) for part in self.parts)
