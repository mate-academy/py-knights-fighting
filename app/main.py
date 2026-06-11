from app.knight import Knight


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
    lancelot_data = knights_config["lancelot"]
    lancelot = Knight(
        name=lancelot_data["name"],
        power=lancelot_data["power"],
        hp=lancelot_data["hp"],
        armour=lancelot_data["armour"],
        weapon=lancelot_data["weapon"],
        potion=lancelot_data["potion"]
    )

    red_knight_data = knights_config["red_knight"]
    red_knight = Knight(
        name=red_knight_data["name"],
        power=red_knight_data["power"],
        hp=red_knight_data["hp"],
        armour=red_knight_data["armour"],
        weapon=red_knight_data["weapon"],
        potion=red_knight_data["potion"]
    )

    mordred_data = knights_config["mordred"]
    mordred = Knight(
        name=mordred_data["name"],
        power=mordred_data["power"],
        hp=mordred_data["hp"],
        armour=mordred_data["armour"],
        weapon=mordred_data["weapon"],
        potion=mordred_data["potion"]
    )

    arthur_data = knights_config["arthur"]
    arthur = Knight(
        name=arthur_data["name"],
        power=arthur_data["power"],
        hp=arthur_data["hp"],
        armour=arthur_data["armour"],
        weapon=arthur_data["weapon"],
        potion=arthur_data["potion"]
    )

    lancelot.prepare_for_battle()
    red_knight.prepare_for_battle()
    mordred.prepare_for_battle()
    arthur.prepare_for_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # 1 Lancelot vs Mordred:
    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # 2 Arthur vs Red Knight:
    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
