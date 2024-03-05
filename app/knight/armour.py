class Armour:
    def __init__(self, parameters: dict) -> None:
        self.part = parameters["part"]
        self.protection = parameters["protection"]

    def __repr__(self):
        return f"{self.part} {self.protection}"

    def __str__(self):
        return f"{self.part} {self.protection}"
