class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name: str = name
        self.protection: int = protection

    def __repr__(self) -> str:
        return f"Armour(name={self.name}, protection={self.protection})"
