from dataclasses import dataclass, field


@dataclass
class Armour:
    armour: list = field(repr=False, default_factory=list)
    helmet: dict = field(init=False, default=None)
    breastplate: dict = field(init=False, default=None)
    boots: dict = field(init=False, default=None)
    total_protection: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        for item in self.armour:
            self.total_protection += item["protection"]
            if item["part"] == "helmet":
                self.helmet = {"protection": item["protection"]}
            elif item["part"] == "breastplate":
                self.breastplate = {"protection": item["protection"]}
            else:
                self.boots = {"protection": item["protection"]}
