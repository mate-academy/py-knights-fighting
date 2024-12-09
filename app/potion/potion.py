from __future__ import annotations


class Potion:
    def __init__(self, name: str, effects: dict) -> None:
        self.name = name
        self.effects = effects

    @classmethod
    def create_potion(cls, potion_config: dict) -> Potion | None:
        if potion_config:
            return cls(
                name=potion_config["name"],
                effects=potion_config["effect"]
            )
        return None

    def __str__(self) -> str:
        return f"Potion: {self.name}\nEffects: {self.effects}"
