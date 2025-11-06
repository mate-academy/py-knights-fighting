class Armour:

    def __init__(self, part: str, protection: int = 0) -> None:
        self.part = part
        self.protection = protection

    def __str__(self) -> None:
        print(f"{self.part} has {self.protection} protection")
