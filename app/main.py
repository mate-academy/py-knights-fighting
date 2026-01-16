from app.khights import Knight, duel

base_knights_config = {
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


def battle(base_knights_config: dict) -> dict:
    lancelot = Knight(name=base_knights_config["lancelot"]["name"],
                      power=base_knights_config["lancelot"]["power"],
                      hp=base_knights_config["lancelot"]["hp"],
                      armour=base_knights_config["lancelot"]["armour"],
                      weapon=base_knights_config["lancelot"]["weapon"],
                      potion=base_knights_config["lancelot"]["potion"])

    arthur = Knight(name=base_knights_config["arthur"]["name"],
                    power=base_knights_config["arthur"]["power"],
                    hp=base_knights_config["arthur"]["hp"],
                    armour=base_knights_config["arthur"]["armour"],
                    weapon=base_knights_config["arthur"]["weapon"],
                    potion=base_knights_config["arthur"]["potion"])

    mordred = Knight(name=base_knights_config["mordred"]["name"],
                     power=base_knights_config["mordred"]["power"],
                     hp=base_knights_config["mordred"]["hp"],
                     armour=base_knights_config["mordred"]["armour"],
                     weapon=base_knights_config["mordred"]["weapon"],
                     potion=base_knights_config["mordred"]["potion"])

    red_knight = Knight(name=base_knights_config["red_knight"]["name"],
                        power=base_knights_config["red_knight"]["power"],
                        hp=base_knights_config["red_knight"]["hp"],
                        armour=base_knights_config["red_knight"]["armour"],
                        weapon=base_knights_config["red_knight"]["weapon"],
                        potion=base_knights_config["red_knight"]["potion"])

    for knight in (lancelot, arthur, mordred, red_knight):
        knight.prepare_for_battle()

    duel(lancelot, mordred)

    duel(arthur, red_knight)

    for knight in (lancelot, arthur, mordred, red_knight):
        if knight.is_dead():
            knight.hp = 0

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}
