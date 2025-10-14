from typing import Optional, Dict


class Potion:
    def __init__(self, data: Optional[Dict] = None) -> None:
        self.name = data.get("name") if data else "None"
        self.effect = data.get("effect", {}) if data else {}

    def get_effect(self, stat: str) -> int:
        return self.effect.get(stat, 0)
