from app.knights.knight import Knight


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
    knight1 = Knight(knights_config["lancelot"])
    knight2 = Knight(knights_config["mordred"])
    knight3 = Knight(knights_config["arthur"])
    knight4 = Knight(knights_config["red_knight"])
    knights = [knight1, knight2, knight3, knight4]

    for knight in knights:
        if knight.potion is not None:
            if "power" in knight.potion.effect:
                knight.power += knight.potion.effect["power"]

            if "protection" in knight.potion.effect:
                knight.protection += knight.potion.effect["protection"]

            if "hp" in knight.potion.effect:
                knight.hp += knight.potion.effect["hp"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection
    knight3.hp -= knight4.power - knight3.protection
    knight4.hp -= knight3.power - knight4.protection

    # check if someone fell in battle
    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0

    if knight3.hp <= 0:
        knight3.hp = 0

    if knight4.hp <= 0:
        knight4.hp = 0

    # Return battle results:
    return {
        knight1.name: knight1.hp,
        knight3.name: knight3.hp,
        knight2.name: knight2.hp,
        knight4.name: knight4.hp,
    }
