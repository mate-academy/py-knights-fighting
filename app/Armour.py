class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.__part: str = part
        self.__protection: int = protection

    @property
    def part(self) -> str:
        return self.__part

    @property
    def protection(self) -> int:
        return self.__protection

    def __repr__(self) -> str:
        return f"Armour(name='{self.part}', protection={self.protection})"
