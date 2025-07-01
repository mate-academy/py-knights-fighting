from __future__ import annotations


class Effect:
    def __init__(self,
                 power: int = None,
                 hp: int = None,
                 protection: int = None) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def from_dict(cls, data: dict) -> Effect | None:
        if not data:
            return None

        return cls(
            power=data.get("power"),
            hp=data.get("hp"),
            protection=data.get("protection")
        )
