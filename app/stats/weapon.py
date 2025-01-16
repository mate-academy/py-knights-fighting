from dataclasses import dataclass, field


@dataclass
class Weapon:
    weapons: dict = field(repr=False, default_factory=dict)
    name: str = field(init=False)
    power: int = field(init=False)

    def __post_init__(self) -> None:
        self.name = self.weapons["name"]
        self.power = self.weapons["power"]
