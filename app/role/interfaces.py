from typing import Protocol


class PotionTarget(Protocol):
    power: int
    hp: float
    protection: int
