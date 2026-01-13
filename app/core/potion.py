from __future__ import annotations

from app.core.effect import Effect


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def init_from_dict(cls, potion_dict: dict) -> Potion | None:
        if not potion_dict:
            return None
        return cls(potion_dict["name"],
                   Effect.init_from_dict(potion_dict["effect"]))
