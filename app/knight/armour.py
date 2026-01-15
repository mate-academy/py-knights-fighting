class Armour:
    def __init__(self, parameters: dict) -> None:
        self.part = parameters["part"]
        self.protection = parameters["protection"]

    def __repr__(self) -> str:
        return f"{self.part} {self.protection}"

    def __str__(self) -> str:
        return f"{self.part} {self.protection}"
