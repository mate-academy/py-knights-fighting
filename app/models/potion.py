from __future__ import annotations

from app.models.effect import Effect


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def from_dict(cls, data: dict) -> Potion | None:
        if not data:
            return None

        effect = Effect.from_dict(data.get("effect"))

        return cls(name=data.get("name"), effect=effect)
