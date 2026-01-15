class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __str__(self) -> str:
        return f"{self.part}: {self.protection} protection"

    def __repr__(self) -> str:
        return self.__str__()
