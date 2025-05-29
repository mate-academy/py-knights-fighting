from typing import Dict, Optional


class Potion:
    def __init__(
        self,
        name: Optional[str],
        effect: Optional[Dict[str, int]] = None
    ) -> None:
        self.name = name
        self.effect = effect or {}

    def __repr__(self) -> str:
        return f"Potion(name='{self.name}', effect={self.effect})"
