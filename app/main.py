from app.models.armour import Armour
from app.models.knight import Knight
from app.models.potion import Potion
from app.models.weapon import Weapon
from app.services.arena import Arena


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
    """
    Executes the battles based on the configuration dictionary.

    Transforms raw dictionary configs into object-oriented instances,
    runs the combat inside the Arena, and returns the final HP results.
    """
    # 1. Parse and instantiate all Knights dynamically
    knights = {}
    for key, data in knights_config.items():
        # Build weapon instance
        weapon_data = data["weapon"]
        weapon = Weapon(name=weapon_data["name"], power=weapon_data["power"])

        # Build armour instance
        armour = Armour(armour_list=data.get("armour", []))

        # Build potion instance if it exists
        potion_data = data.get("potion")
        potion = (
            Potion(name=potion_data["name"], effect=potion_data.get("effect"))
            if potion_data
            else None
        )

        # Build full knight instance
        knights[key] = Knight(
            name=data["name"],
            base_hp=data["hp"],
            base_power=data["power"],
            armour=armour,
            weapon=weapon,
            potion=potion,
        )

    # 2. Setup the defined matchups
    # Matchup 1: Lancelot vs Mordred
    arena_1 = Arena(knights["lancelot"], knights["mordred"])
    arena_1.battle()

    # Matchup 2: Arthur vs Red Knight
    arena_2 = Arena(knights["arthur"], knights["red_knight"])
    arena_2.battle()

    # 3. Format and return the final dictionary to pass the tests
    # Ensure we use the proper display names (e.g., "Red Knight") as keys
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }
