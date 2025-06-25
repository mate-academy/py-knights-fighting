from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return (
            f"Armour("
            f"part = '{self.part}', "
            f"protection = {self.protection}"
            f")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def create_from_dict(cls, data: dict) -> Armour | None:
        if not data:
            return None

        part = data.get("part", "")
        protection = data.get("protection", 0)

        return cls(part, protection)
