from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.knights.knight import Knight


class Potion:
    def __init__(self, data: Optional[dict]) -> None:
        # data may be None
        self.name: str = ""
        self.effect: dict = {}
        if data:
            self.name = data.get("name", "")
            self.effect = data.get("effect", {}) or {}

    def apply_effect(self, knight: "Knight") -> None:
        knight.hp += int(self.effect.get("hp", 0))
        knight.power += int(self.effect.get("power", 0))
        knight.protection += int(self.effect.get("protection", 0))
