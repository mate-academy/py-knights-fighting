from typing import Dict, Any


class Potion:
    def __init__(self, name: str, effect: Dict[str, Any]) -> None:
        self.name = name
        self.effect = effect

    # Zwraca bonus HP z mikstury
    def extra_hp(self) -> int:
        return self.effect.get("hp", 0)

    # Zwraca bonus power z mikstury
    def extra_power(self) -> int:
        return self.effect.get("power", 0)

    # Zwraca bonus protection z mikstury
    def extra_protection(self) -> int:
        return self.effect.get("protection", 0)
