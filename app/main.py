from app.knights.knight import Knight
from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion


def prepare_knight(data: dict) -> Knight:
    knight = Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"]
    )

    weapon_data = data.get("weapon")
    if weapon_data:
        weapon = Weapon(
        name=weapon_data["name"],
        power=weapon_data["power"]
        )
        knight.equip_weapon(weapon)

    for armour_data in data.get("armour", []):
        armour = Armour(
            name=armour_data["part"],
            protection=armour_data["protection"]
        )
        knight.equip_armour(armour)

    potion_data = data.get("potion")
    if potion_data and potion_data.get("effect"):
        potion = Potion(effect=potion_data["effect"])
        knight.drink_potion(potion)

    return knight

def battle(knights_config: dict) -> str:
    lancelot = prepare_knight(knights_config["lancelot"])
    mordred = prepare_knight(knights_config["mordred"])

    while lancelot.hp > 0 and mordred.hp > 0:
        damage_to_mordred = max(0, lancelot.power - mordred.protection)
        damage_to_lancelot = max(0, mordred.power - lancelot.protection)

        mordred.hp -= damage_to_mordred
        lancelot.hp -= damage_to_lancelot

        if mordred.hp <= 0 and lancelot.hp <= 0:
            mordred.hp = 0
            lancelot.hp = 0
            return lancelot.name

        if mordred.hp <= 0:
            mordred.hp = 0
            return lancelot.name

        if lancelot.hp <= 0:
            lancelot.hp = 0
            return mordred.name

    if lancelot.hp > 0:
        return lancelot.name
    return mordred.name


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
