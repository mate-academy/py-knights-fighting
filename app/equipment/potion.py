from __future__ import annotations

from app.equipment.effect import Effect


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect

    def __repr__(self) -> str:
        return (
            f"Potion("
            f"name = '{self.name}', "
            f"effect = {self.effect}"
            f")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def create_from_dict(cls, data: dict) -> Potion | None:
        if not data:
            return None

        name = data.get("name", "")
        effect = Effect.create_from_dict(data.get("effect"))

        return cls(name, effect)
