from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_dict_list(cls, data: dict) -> list[Armour] | None:
        if not data:
            return None

        armours = []

        for armour in data:
            armours.append(Armour.from_dict(armour))

        return armours

    @classmethod
    def from_dict(cls, data: dict) -> Armour:
        return cls(part=data.get("part"), protection=data.get("protection"))
