class Equipment:
    """Base class for all equipment types."""

    def __init__(self, name: str) -> None:
        self.name = name


class Weapon(Equipment):
    """Represents a weapon with a power attribute."""

    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power


class Armour(Equipment):
    """Represents a piece of armor with a protection value."""

    def __init__(self, part: int, protection: str) -> None:
        super().__init__(part)
        self.protection = protection


class Potion(Equipment):
    """Represents a potion with various effects."""

    def __init__(self, name: str, effect: str) -> None:
        super().__init__(name)
        self.effect = effect
