from typing import Dict, Optional, List

class Item:
    def __init__(self, name: str):
        self.name = name

class Weapon(Item):
    def __init__(self, name: str, power: int):
        super().__init__(name)
        self.power = power

class Armor(Item):
    def __init__(self, name: str, part: str, protection: int):
        super().__init__(name)
        self.part = part
        self.protection = protection

class Potion(Item):
    def __init__(self, name: str, effect: Optional[Dict[str, int]] = None):
        super().__init__(name)
        self.effect = effect if effect else {}
