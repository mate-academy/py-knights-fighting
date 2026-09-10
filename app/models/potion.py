from dataclasses import dataclass
from .status import Status


@dataclass
class Potion:
    name: str
    effect: Status