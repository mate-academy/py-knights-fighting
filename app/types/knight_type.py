from typing import TypedDict


class ArmourType(TypedDict):
    part: str
    protection: int


class WeaponType(TypedDict):
    name: str
    power: int


class PotionEffect(TypedDict):
    hp: int
    power: int


class PotionType(TypedDict):
    name: str
    effect: PotionEffect


class KnightType(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[ArmourType]
    weapon: WeaponType
    potion: PotionType | None
    protection: int
