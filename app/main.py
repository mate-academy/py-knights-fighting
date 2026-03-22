from app.warrior.knight import Knight


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


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.stats -= knight2.stats
    knight2.stats -= knight1.stats
    if knight1.stats.hp < 0:
        knight1.stats.hp = 0
    if knight2.stats.hp < 0:
        knight2.stats.hp = 0

    if knight1.stats.hp > knight2.stats.hp:
        print(f"{knight2.name} was defeated by {knight1.name}")
    elif knight2.stats.hp > knight1.stats.hp:
        print(f"{knight1.name} was defeated by {knight2.name}")
    else:
        print("Draw")
    print(f"{knight1.name} hp: {knight1.stats.hp}")
    print(f"{knight2.name} hp: {knight2.stats.hp}")


def battle(knights_config: dict) -> dict[str, int]:
    knight_dict = {knight_name : Knight(knight_stats)
                   for knight_name, knight_stats in knights_config.items()}
    duel(knight_dict["lancelot"], knight_dict["mordred"])
    duel(knight_dict["arthur"], knight_dict["red_knight"])
    return {knight.name : knight.stats.hp for knight in knight_dict.values()}



if __name__ == "__main__":
    print(battle(KNIGHTS))
