from typing import List, Dict, Optional


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: Dict[str, int]) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armour: List[Dict[str, int]],
        weapon: Dict[str, int],
        potion: Optional[Dict] = None,
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = [Armour(a["part"], a["protection"]) for a in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(potion["name"]
                             , potion["effect"]) if potion else None
        self.apply_equipment()

    def apply_equipment(self) -> None:
        """Applies armour, weapon, and potion effects to the knight's stats."""
        self.protection = sum(a.protection for a in self.armour)
        self.power = self.base_power + self.weapon.power
        self.hp = self.base_hp

        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, attack_power: int) -> None:
        damage = max(0, attack_power - self.protection)
        self.hp = max(0, self.hp - damage)


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    """Runs battles between knights and returns the final HP values."""
    knights = {name: Knight(
        name=data["name"],
        base_power=data["power"],
        base_hp=data["hp"],
        armour=data["armour"],
        weapon=data["weapon"],
        potion=data.get("potion")
    ) for name, data in knights_config.items()}

    # First battle: Lancelot vs. Mordred
    knights["lancelot"].take_damage(knights["mordred"].power)
    knights["mordred"].take_damage(knights["lancelot"].power)

    # Second battle: Arthur vs. Red Knight
    knights["arthur"].take_damage(knights["red_knight"].power)
    knights["red_knight"].take_damage(knights["arthur"].power)

    return {knight.name: knight.hp for knight in knights.values()}


# Sample knight configuration
KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {
            "name": "Berserk",
            "effect": {"power": 15, "hp": -5, "protection": 10},
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
    },
}

if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
