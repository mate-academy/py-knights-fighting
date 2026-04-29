class Armour:
    def __init__(self, armour_element: dict) -> None:
        self._name = armour_element["part"]
        self._protection = armour_element["protection"]

    @property
    def part(self) -> str:
        return self._name

    @property
    def protection(self) -> int:
        return self._protection
