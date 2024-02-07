from __future__ import annotations

from app.arsenal.effect import Effect


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect

    @staticmethod
    def convert_to_potion(potion: dict) -> Potion | None:
        if potion is None:
            return None
        effect = potion.get("effect")
        return Potion(
            name=potion["name"],
            effect=Effect(
                hp=effect.get("hp", 0),
                power=effect.get("power", 0),
                protection=effect.get("protection", 0)
            )
        )
