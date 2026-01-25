class Armor:
    def __init__(self, parts: list[dict]) -> None:
        self.parts = parts

    def total_armor(self) -> int:
        total_armor = 0
        for part in self.parts:
            total_armor += part["protection"]

        return total_armor
