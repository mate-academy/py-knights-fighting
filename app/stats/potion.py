from dataclasses import dataclass, field


@dataclass
class Potion:
    potion: dict = field(repr=False, default=None)
    name: str = field(init=False, default=None)
    effects: dict = field(init=False, repr=False, default_factory=dict)
    power: int = field(init=False, default=None)
    hp: int = field(init=False, default=None)
    protection: int = field(init=False, default=None)

    def __post_init__(self) -> None:
        if self.potion is not None:
            # init all others data
            self.name = self.potion["name"]
            self.effects = self.potion["effect"]
            self.power = self.effects.get("power", 0)
            self.hp = self.effects.get("hp", 0)
            self.protection = self.effects.get("protection", 0)
