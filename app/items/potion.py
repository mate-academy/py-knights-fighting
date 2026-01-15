from typing import Optional


class Potion:
    def __init__(
            self,
            name: str,
            effect: Optional[dict] = None,
            hp: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.hp = effect.get("hp", 0) if effect else hp
        self.power = effect.get("power", 0) if effect else power
        self.protection = effect.get("protection", 0) if effect else protection
