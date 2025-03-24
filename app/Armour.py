class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.__name: str = name
        self.__protection: int = protection

    @property
    def name(self) -> str:
        return self.__name

    @property
    def protection(self) -> int:
        return self.__protection

    def __repr__(self) -> str:
        return f"Armour(name='{self.name}', protection={self.protection})"
