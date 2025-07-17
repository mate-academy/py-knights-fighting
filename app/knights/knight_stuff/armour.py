class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    def __repr__(self) -> str:
        return f"Armour(part={self.name}, protection={self.protection})"
