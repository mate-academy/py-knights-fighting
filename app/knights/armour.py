class Armour:
    def __init__(self, part: str, protection: str) -> None:
        self.part = part
        self.protection = protection

    def __str__(self) -> None:
        return f"{self.part} (+{self.protection} Protection)"
