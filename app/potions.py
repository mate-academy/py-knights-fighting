from __future__ import annotations


class Potion:
    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def create_potion(cls, info: dict) -> Potion | None:
        if not info:
            return None
        potion = cls(info["name"])

        if info["effect"].get("hp"):
            potion.hp = info["effect"]["hp"]

        if info["effect"].get("power"):
            potion.power = info["effect"]["power"]

        if info["effect"].get("protection"):
            potion.protection = info["effect"]["protection"]

        return potion
