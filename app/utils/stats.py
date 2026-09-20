class Armour:
    """Armour piece with protection value."""

    part: str
    protection: int | float

    def __init__(self, part: str, protection: int | float) -> None:
        """Initialize armour piece."""
        self.part = part
        self.protection = protection


class Weapon:
    """Weapon with power value."""

    name: str
    power: int | float

    def __init__(self, name: str, power: int | float) -> None:
        """Initialize weapon."""
        self.name = name
        self.power = power


class Potion:
    """Potion with stat effects."""

    name: str
    effect: dict[str, int | float]

    def __init__(
        self, name: str, effect: dict[str, int | float]
    ) -> None:
        """Initialize potion with effects."""
        self.name = name
        self.effect = effect
