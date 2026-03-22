from app.items.items_by_knight import Armour, Weapon, Potion
from app.knight_maker.new_knight import Knight


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


def fight(knight1: Knight, knight2: Knight) -> dict:
    k1_stats = knight1.prepare_stats()
    k2_stats = knight2.prepare_stats()
    damage1 = max(0, k2_stats["power"] - k1_stats["protection"])
    hp1 = max(0, k1_stats["hp"] - damage1)
    damage2 = max(0, k1_stats["power"] - k2_stats["protection"])
    hp2 = max(0, k2_stats["hp"] - damage2)
    return {knight1.name: hp1, knight2.name: hp2}


def battle(knights_config: dict) -> dict:
    knights = []
    battle1 = {}
    battle2 = {}

    for knight in knights_config.values():
        k_weapon = knight.get("weapon") or {}
        weapon = Weapon(k_weapon.get("name"), k_weapon.get("power"))
        k_armour = knight.get("armour") or []
        armour = [
            Armour(piece["part"], piece["protection"])
            for piece in k_armour]
        potion = None
        if knight.get("potion"):
            k_potion = knight.get("potion")
            potion = Potion(k_potion.get("name"), k_potion.get("effect"))

        knight_conf = Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            weapon=weapon,
            armour=armour,
            potion=potion)
        knights.append(knight_conf)

    if len(knights) >= 4:
        battle1 = fight(knights[0], knights[2])
        battle2 = fight(knights[1], knights[3])
    return {**battle1, **battle2}
