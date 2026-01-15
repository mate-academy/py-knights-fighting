class Armour:
    def __init__(self, armour: list[dict]) -> None:
        self.protection = sum(item["protection"] for item in armour)
