from app.armour import Armour
from app.knight import Knight
from app.potion import Potion
from app.weapon import Weapon

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


def create_knight(knight_dict: dict) -> Knight:
    armours = []
    if knight_dict["armour"] is not None:
        for armour_dict in knight_dict["armour"]:
            armours.append(Armour(armour_dict["part"],
                                  armour_dict["protection"]))
    weapon = Weapon(knight_dict["weapon"]["name"],
                    knight_dict["weapon"]["power"])
    if knight_dict["potion"] is None:
        potion = None
    else:
        if knight_dict["potion"]["effect"].get("protection") is None:
            potion = Potion(knight_dict["potion"]["name"],
                            knight_dict["potion"]["effect"]["hp"],
                            knight_dict["potion"]["effect"]["power"], None)
        else:
            potion = Potion(knight_dict["potion"]["name"],
                            knight_dict["potion"]["effect"]["hp"],
                            knight_dict["potion"]["effect"]["power"],
                            knight_dict["potion"]["effect"]["protection"])
    power = knight_dict["power"]
    if "power" in knight_dict["weapon"]:
        power += knight_dict["weapon"]["power"]
    if knight_dict["potion"] and "power" in knight_dict["potion"]["effect"]:
        power += knight_dict["potion"]["effect"]["power"]
    hp = knight_dict["hp"]
    if knight_dict["potion"] and "hp" in knight_dict["potion"]["effect"]:
        hp += knight_dict["potion"]["effect"]["hp"]
    return Knight(knight_dict["name"], power, hp, armours, weapon, potion)


def battle(knights_config: dict) -> dict:
    # -------------------------------------------------------------------------------
    # BATTLE:

    lancelot = create_knight(knights_config["lancelot"])
    arthur = create_knight(knights_config["arthur"])
    mordred = create_knight(knights_config["mordred"])
    red_knight = create_knight(knights_config["red_knight"])

    lancelot.hp -= mordred.power - lancelot.count_protection()
    mordred.hp -= lancelot.power - mordred.count_protection()

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.count_protection()
    red_knight.hp -= arthur.power - red_knight.count_protection()

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
