from __future__ import annotations


class Potion:
    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def create_potion(cls, info: dict) -> Potion | None:
        if not info:
            return None
        potion = cls(info["name"])

        for attr in ["hp", "power", "protection"]:
            if info["effect"].get(attr):
                setattr(potion, attr, info["effect"][attr])

        return potion
