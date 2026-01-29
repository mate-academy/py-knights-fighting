from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.fighter.fighter import Fighter

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
    knights = dict()

    for knight in knights_config.values():
        armours = []
        for armour_part in knight["armour"]:
            armours.append(Armour(armour_part.get("part"),
                                  armour_part.get("protection")))
        weapon = Weapon(knight["weapon"]["name"], knight["weapon"]["power"])
        potion = Potion(knight["potion"]["name"],
                        knight["potion"]["effect"]
                        )if knight["potion"] else None
        fighter = Fighter(
            knight["name"],
            knight["power"],
            knight["hp"],
            armours,
            weapon,
            potion
        )
        fighter.apply_armour()
        fighter.equip_weapon()
        fighter.drink_potion()
        knights[fighter.name] = fighter

    battle_results = dict()

    def fight(fighter_a: Fighter, fighter_b: Fighter) -> None:
        fighter_a.hp -= fighter_b.power - fighter_a.protection
        fighter_b.hp -= fighter_a.power - fighter_b.protection
        fighter_a.hp = max(0, fighter_a.hp)
        fighter_b.hp = max(0, fighter_b.hp)
        battle_results[fighter_a.name] = fighter_a.hp
        battle_results[fighter_b.name] = fighter_b.hp

    fight(knights["Lancelot"], knights["Mordred"])
    fight(knights["Arthur"], knights["Red Knight"])

    return battle_results
