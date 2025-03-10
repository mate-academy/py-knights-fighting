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


def prepare_knight(knight_data: dict) -> dict:
    """Застосовує броню, зброю та зілля до лицаря."""
    knight = knight_data.copy()
    knight["protection"] = sum(armour["protection"]
                               for armour in knight["armour"])
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"]:
        effect = knight["potion"]["effect"]
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)
    return knight


def battle_round(knight1: dict, knight2: dict) -> None:
    """Виконує один раунд бою між двома лицарями."""
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def format_results(knights: dict) -> dict:
    """Форматує результати бою у вигляді словника."""
    return {knight["name"]: knight["hp"] for knight in knights.values()}


def battle(knights_config: dict) -> dict:
    prepared_knights = {name: prepare_knight(data)
                        for name, data in knights_config.items()}
    knights_list = list(prepared_knights.values())

    battle_round(knights_list[0], knights_list[2])  # Lancelot vs Mordred
    battle_round(knights_list[1], knights_list[3])  # Arthur vs Red Knight

    return format_results(prepared_knights)


print(battle(KNIGHTS))
