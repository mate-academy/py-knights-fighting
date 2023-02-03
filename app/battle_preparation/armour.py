class Armour:

    def __init__(self, armors: list) -> None:
        self.name = [name["part"] for name in armors]
        self.protection = sum(power["protection"] for power in armors)

    def __str__(self) -> str:
        return f"Armour protection {self.protection}"
