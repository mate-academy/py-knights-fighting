from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.knights.knight import Knight


class Potion:
    def __init__(self, effect: dict) -> None:
        self.effect = effect

    def apply(self, knight: "Knight") -> None:
        for stat, value in self.effect.items():
            setattr(knight, stat, getattr(knight, stat) + value)
