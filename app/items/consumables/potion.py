from __future__ import annotations


class Potion:
    def __init__(self, data: dict) -> None:
        if data is None:
            self.power = 0
            self.hp = 0
            self.protection = 0
        else:
            effect = data["effect"]
            self.name = data["name"]
            self.power = effect.get("power", 0)
            self.hp = effect.get("hp", 0)
            self.protection = effect.get("protection", 0)
