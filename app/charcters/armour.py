from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __str__(self) -> str:
        return f"Armour(part= {self.part}, protection={self.protection})"
