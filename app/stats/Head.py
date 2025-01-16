from dataclasses import dataclass, field


@dataclass()
class Main:
    name: str
    power: int
    hp: int
    protection: int = field(default=0, init=False)

    def boost(self, extra_power: int) -> int:
        self.power += extra_power
        return self.power
