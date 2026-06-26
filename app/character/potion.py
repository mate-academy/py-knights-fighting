from dataclasses import dataclass

from app.character.effect import Effect


@dataclass
class Potion:
    name: str
    effect: Effect
