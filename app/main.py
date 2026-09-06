from typing import List, TypedDict


class Armour(TypedDict):
    part: str
    protection: int


class Weapon(TypedDict):
    name: str
    power: int


class Potion(TypedDict):
    name: str
    effect: dict[str, int]


class KnightStats(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Potion | None


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: List[Armour],
                 weapon: Weapon,
                 potion: Potion | None) -> None:
        self.name = name
        actual_power = power + weapon["power"]
        actual_hp = hp
        actual_protection = 0
        for part in armour:
            actual_protection += part.get("protection", 0)

        if potion is not None:
            for stat, num in potion["effect"].items():
                if stat == "hp":
                    actual_hp += int(num)
                elif stat == "power":
                    actual_power += int(num)
                elif stat == "protection":
                    actual_protection += int(num)

        self.power = actual_power
        self.hp = actual_hp
        self.protection = actual_protection


KNIGHTS: dict[str, KnightStats] = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle_between_two(first: Knight, second: Knight) -> None:
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection
    if first.hp <= 0:
        first.hp = 0

    if second.hp <= 0:
        second.hp = 0


def battle(knights: dict[str, KnightStats]) -> dict[str, int]:
    knights_stats: dict[str, Knight] = dict()
    for knight, stats in knights.items():
        knights_stats[knight] = Knight(**stats)

    battle_between_two(knights_stats["lancelot"], knights_stats["mordred"])
    battle_between_two(knights_stats["arthur"], knights_stats["red_knight"])

    return ({knights_stats["lancelot"].name: knights_stats["lancelot"].hp,
             knights_stats["arthur"].name: knights_stats["arthur"].hp,
             knights_stats["mordred"].name: knights_stats["mordred"].hp,
             knights_stats["red_knight"].name: knights_stats["red_knight"].hp})


print(battle(KNIGHTS))
