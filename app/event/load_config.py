from __future__ import annotations
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.people.knight import Knight


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


def load_config(config_knights: dict) -> None:

    Knight.knights_dict = {}
    for knight_keys in config_knights.values():

        current_armour_list = []
        for armour_dict in knight_keys.get("armour"):
            current_armour_list.append(
                Armour(part=armour_dict.get("part"),
                       protection=armour_dict.get("protection")))

        current_weapon = None
        weapon_dict = knight_keys.get("weapon")
        if weapon_dict:
            current_weapon = Weapon(name=weapon_dict.get("name"),
                                    power=weapon_dict.get("power"))

        current_potion = None
        potion_dict = knight_keys.get("potion")
        if potion_dict and "effect" in potion_dict:
            potion_effects = potion_dict.get("effect")
            if potion_effects and isinstance(potion_effects, dict):
                current_potion = Potion(
                    name=potion_dict.get("name"),
                    effect_power=potion_effects.get("power") or 0,
                    effect_hp=potion_effects.get("hp") or 0,
                    effect_protection=potion_effects.get("protection") or 0)

        Knight(name=knight_keys.get("name"),
               power=knight_keys.get("power"),
               hp=knight_keys.get("hp"),
               armour=current_armour_list,
               weapon=current_weapon,
               potion=current_potion)
