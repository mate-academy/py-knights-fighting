from typing import Optional, TypedDict, List, NotRequired


class Armour(TypedDict):
    name: str
    protection: int


class Weapon(TypedDict):
    name: str
    power: int


class Effect(TypedDict):
    hp: NotRequired[int]
    power: NotRequired[int]
    protection: NotRequired[int]


class Potion(TypedDict):
    name: str
    effect: Effect


class Knight(TypedDict):
    name: str
    power: int
    hp: int
    armour: List[Optional[Armour]]
    weapon: Weapon
    potion: Potion | None


class KnightDict(TypedDict):
    [str, Knight]
