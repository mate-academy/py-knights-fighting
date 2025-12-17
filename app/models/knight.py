from typing import Literal, Optional, TypedDict, List, NotRequired, Dict


class Armour(TypedDict):
    part: str
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


KnightName = Literal["lancelot", "arthur", "mordred", "red_knight"]


class Knight(TypedDict):
    name: KnightName
    power: int
    hp: int
    armour: List[Optional[Armour]]
    weapon: Weapon
    potion: Potion | None


KnightDict = Dict[str, Knight]
