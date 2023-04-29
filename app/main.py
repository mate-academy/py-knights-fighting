KNIGHTS = {
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


class Knight:
    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.power = stats["power"] + stats["weapon"]["power"]
        self.protection = sum(arm["protection"] for arm in stats["armour"])
        self.hp = stats["hp"]

        if stats["potion"] is not None:
            if stats["potion"]["effect"].get("hp"):
                self.hp += stats["potion"]["effect"]["hp"]
            if stats["potion"]["effect"].get("power"):
                self.power += stats["potion"]["effect"]["power"]
            if stats["potion"]["effect"].get("protection"):
                self.protection += stats["potion"]["effect"]["protection"]


def battle(knights_config: dict) -> dict:
    # Announce the knights
    knights = [Knight(knights_config[knight]) for knight in knights_config]

    # Battle pairs
    battles = [(knights[0], knights[2]), (knights[1], knights[3])]

    # Result HP
    result_hp = dict()

    # Battle
    for knight1, knight2 in battles:
        knight1.hp -= (knight2.power - knight1.protection)
        knight2.hp -= knight1.power - knight2.protection
        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0
        result_hp[knight1.name] = knight1.hp
        result_hp[knight2.name] = knight2.hp

    # Results
    return result_hp
