from typing import Optional, TypedDict


class Effect(TypedDict, total=False):
    power: Optional[int]
    hp: Optional[int]
    protection: Optional[int]
