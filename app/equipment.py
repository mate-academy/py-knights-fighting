class ArmourPart:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(
        self,
        name: str,
        effect: dict[str, int] | None = None,
    ) -> None:
        self.name = name
        self.effect = effect or {}
