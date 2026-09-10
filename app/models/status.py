from dataclasses import dataclass


@dataclass
class Status:
    power: int | None
    hp: int | None
    protection: int | None