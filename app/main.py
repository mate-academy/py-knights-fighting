from app.battle.battle_action import Battle
from app.battle_preparations.inventory import Inventory

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


def battle(knights_config: dict) -> dict:
    inventory = Inventory()
    battle_action = Battle()

    # apply inventory
    for knight, knight_stats in knights_config.items():
        print(f"{knight}: {knight_stats}")
        knight_stats["protection"] = inventory.apply_armour(
            knight_stats["armour"]
        )
        print(f"after armour: {knight}: {knight_stats}")
        knight_stats["power"] = inventory.apply_weapon(
            knight_stats["power"],
            knight_stats["weapon"]
        )
        print(f"after weapon: {knight}: {knight_stats}")
        knight_stats = inventory.apply_potion(knight_stats)
        print(f"after potion: {knight}: {knight_stats}\n")

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights_config["lancelot"]["hp"] = battle_action.do_battle(
        knights_config["lancelot"]["hp"],
        knights_config["mordred"]["power"],
        knights_config["lancelot"]["protection"]
    )
    knights_config["mordred"]["hp"] = battle_action.do_battle(
        knights_config["mordred"]["hp"],
        knights_config["lancelot"]["power"],
        knights_config["mordred"]["protection"]
    )
    print(f"after battle: {knights_config["lancelot"]}")
    print(f"after battle: {knights_config["mordred"]}\n")

    # 2 Arthur vs Red Knight:
    knights_config["arthur"]["hp"] = battle_action.do_battle(
        knights_config["arthur"]["hp"],
        knights_config["red_knight"]["power"],
        knights_config["arthur"]["protection"]
    )
    knights_config["red_knight"]["hp"] = battle_action.do_battle(
        knights_config["red_knight"]["hp"],
        knights_config["arthur"]["power"],
        knights_config["red_knight"]["protection"]
    )
    print(f"after battle: {knights_config["arthur"]}")
    print(f"after battle: {knights_config["red_knight"]}\n")

    for knight, knight_stats in knights_config.items():
        print(f"{knight}: {knight_stats}")
        knight_stats["hp"] = battle_action.hp_to_zero(knight_stats["hp"])

    return {
        knights_config[knight]["name"]: knights_config[knight]["hp"]
        for knight in knights_config
    }


print(battle(KNIGHTS))
