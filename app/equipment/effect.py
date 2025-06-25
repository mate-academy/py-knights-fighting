from __future__ import annotations


class Effect:
    def __init__(
        self,
        power: int = 0,
        hp: int = 0,
        protection: int = 0
    ) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection

    def __repr__(self) -> str:
        return (
            f"Effect("
            f"power = {self.power}, "
            f"hp = {self.hp}, "
            f"protection = {self.protection}"
            f")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def create_from_dict(cls, data: dict) -> Effect | None:
        if not data:
            return None

        power = data.get("power", 0)
        hp = data.get("hp", 0)
        protection = data.get("protection", 0)

        return cls(power, hp, protection)
