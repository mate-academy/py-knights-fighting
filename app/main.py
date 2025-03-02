from typing import List, Dict, Optional


class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, armour: List[Dict[str, int]],
                 weapon: Dict[str, int],
                 potion: Optional[Dict[str, Dict[str, int]]]) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.power = self.base_power + self.weapon["power"]
        self.protection = sum(a["protection"] for a in self.armour)
        self.apply_potion()

    def apply_potion(self) -> None:
        if self.potion:
            effects = self.potion["effect"]
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage - self.protection)
        if self.hp < 0:
            self.hp = 0


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    knights = {name: Knight(**data) for name, data in knights_config.items()}

    # Battles
    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for k1, k2 in battles:
        knights[k1].take_damage(knights[k2].power)
        knights[k2].take_damage(knights[k1].power)

    return {knight.name: knight.hp for knight in knights.values()}


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot", "power": 35, "hp": 100, "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50}, "potion": None
    },
    "arthur": {
        "name": "Arthur", "power": 45, "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10}
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55}, "potion": None
    },
    "mordred": {
        "name": "Mordred", "power": 30, "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10}
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {"name": "Berserk", "effect":
                   {"power": +15, "hp": -5,
                    "protection": +10}}
    },
    "red_knight": {
        "name": "Red Knight", "power": 40, "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing", "effect": {"hp": +10, "power": +5}}
    }
}

print(battle(KNIGHTS))
