from typing import Optional, TypedDict, List


class Effect(TypedDict, total=False):
    power: Optional[int]
    hp: Optional[int]
    protection: Optional[int]


type NewKnightsConfig = List[tuple]
