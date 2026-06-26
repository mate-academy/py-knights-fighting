from typing import TypedDict


class EffectDto(TypedDict):
    power: int | None
    hp: int | None
    protection: int | None


class WeaponDto(TypedDict):
    name: str
    power: int


class PotionDto(TypedDict):
    name: str
    effect: EffectDto


class ArmourDto(TypedDict):
    part: str
    protection: int


class CharacterDto(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[ArmourDto]
    weapon: WeaponDto
    potion: PotionDto | None
