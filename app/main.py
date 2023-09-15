from typing import Dict

from app.knights.armour import Armour
from app.knights.knight import Knight
from app.knights.potion import Potion
from app.knights.potion_effect import PotionEffect
from app.knights.weapon import Weapon

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


def initialize_knights(config: Dict[str, Dict]) -> Dict[str, Knight]:
    knights = {}
    for key, k_data in config.items():
        armour_data = k_data.get("armour", [])
        armour = [Armour(a["part"], a["protection"]) for a in armour_data]

        weapon_data = k_data["weapon"]
        weapon = Weapon(weapon_data["name"], weapon_data["power"])

        potion_data = k_data.get("potion", {})
        potion_effect_data = (
            potion_data.get("effect", {})
            if potion_data is not None else {}
        )
        potion_effect = PotionEffect(**potion_effect_data)
        potion = (
            Potion(potion_data.get("name"), potion_effect)
            if potion_data else None
        )

        knight = Knight(
            k_data["name"],
            k_data["power"],
            k_data["hp"],
            armour,
            weapon,
            potion
        )
        knights[key] = knight
    return knights


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    knights = initialize_knights(knights_config)

    for knight in knights.values():
        knight.prepare_for_battle()

    # Lancelot vs Mordred:
    knights["lancelot"].battle(knights["mordred"])
    knights["mordred"].battle(knights["lancelot"])

    # Arthur vs Red Knight:
    knights["arthur"].battle(knights["red_knight"])
    knights["red_knight"].battle(knights["arthur"])

    # Return battle results:
    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
