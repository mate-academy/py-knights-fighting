from typing import Any


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply(self, knight: Any) -> None:
        if "power" in self.effect:
            knight.power += self.effect["power"]

        if "protection" in self.effect:
            if not hasattr(knight, "protection"):
                knight.protection = 0
            knight.protection += self.effect["protection"]

        if "hp" in self.effect:
            knight.hp += self.effect["hp"]
