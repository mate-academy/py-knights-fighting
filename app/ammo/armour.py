class Armour:
    def __init__(self, protection: list[dict]) -> None:
        self.protection = protection

    def total_protection(self) -> int:
        return sum(part["protection"] for part in self.protection)

    def add_protection(self, value: int) -> None:
        self.protection.append(
            {"protection": value}
        )
