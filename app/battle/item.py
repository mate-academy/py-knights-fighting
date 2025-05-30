from typing import Dict, Optional


class Item:
    def __init__(self, name: str) -> None:
        self.name = name


class Weapon(Item):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power


class Armor(Item):
    def __init__(self, name: str, part: str, protection: int) -> None:
        super().__init__(name)
        self.part = part
        self.protection = protection


class Potion(Item):
    def __init__(self, name: str,
                 effect: Optional[Dict[str, int]] = None) -> None:
        super().__init__(name)
        self.effect = effect if effect else {}
