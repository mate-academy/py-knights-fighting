from __future__ import annotations


class Weapon:
    def __init__(
            self,
            name: str,
            power: int
    ) -> None:
        self.name = name
        self.power = power

    @classmethod
    def get_from_dict(cls, weapon_dict: dict[str, str | int]) -> Weapon:
        return cls(
            name=weapon_dict.get("name"),
            power=weapon_dict.get("power")
        )
