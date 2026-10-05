from typing import TypedDict, NotRequired


class Armour(TypedDict):
    part: str
    protection: int


class Weapon(TypedDict):
    name: str
    power: int


class PotionEffect(TypedDict):
    power: NotRequired[int]
    hp: NotRequired[int]
    protection: NotRequired[int]


class Potion(TypedDict):
    name: str
    effect: PotionEffect


class KnightConfig(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Potion | None
