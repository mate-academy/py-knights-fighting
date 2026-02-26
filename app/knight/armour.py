from __future__ import annotations


class Armour:
    def __init__(
            self,
            part: str,
            protection: int
    ) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def get_from_dict(cls, armour_dict: dict[str, str | int]) -> Armour:
        return cls(
            part=armour_dict.get("part"),
            protection=armour_dict.get("protection")
        )
