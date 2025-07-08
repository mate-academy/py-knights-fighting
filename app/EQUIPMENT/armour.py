class Armour:
    def __init__(self, parts: list[dict[str, int]]) -> None:
        self.parts = parts

    def total_protection(self) -> int:
        return sum(part["protection"] for part in self.parts)
