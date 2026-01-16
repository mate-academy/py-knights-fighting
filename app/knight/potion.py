from typing import NamedTuple


class Potion(NamedTuple):
    name: str
    effect: dict[str, int]
