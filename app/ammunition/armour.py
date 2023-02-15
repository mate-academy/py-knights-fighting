class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self._part = part
        self._protection = protection

    @property
    def name(self) -> str:
        return self._part

    @property
    def protection(self) -> int:
        return self._protection
