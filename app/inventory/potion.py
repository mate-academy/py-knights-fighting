from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from app.effect import Effect


@dataclass
class Potion:
    name: str
    effect: Effect

    @classmethod
    def empty(cls) -> Potion:
        return cls("No Potion", Effect(0, 0, 0))

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "Potion":
        if data is None:
            return cls.empty()

        effect_data = data["effect"]
        effect = Effect(
            effect_data.get("hp", 0),
            effect_data.get("power", 0),
            effect_data.get("protection", 0)
        )

        return cls(data["name"], effect)
