from app.knights import Warrior

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


def knight_dict_create(data: dict) -> dict:
    knight_dict = dict()
    knight_dict["name"] = data["name"]
    knight_dict["protection"] = 0
    knight_dict["power"] = data["power"]
    knight_dict["hp"] = data["hp"]
    for armour in data["armour"]:
        knight_dict["protection"] += armour["protection"]

    knight_dict["power"] += data["weapon"]["power"]

    if data["potion"] is not None:
        if "power" in data["potion"]["effect"]:
            knight_dict["power"] += data["potion"]["effect"]["power"]

        if "protection" in data["potion"]["effect"]:
            knight_dict["protection"] += data["potion"]["effect"]["protection"]

        if "hp" in data["potion"]["effect"]:
            knight_dict["hp"] += data["potion"]["effect"]["hp"]

    return knight_dict


def battle(knights: dict) -> dict:
    lancelot_dict = knights["lancelot"]
    arthur_dict = knights["arthur"]
    mordred_dict = knights["mordred"]
    red_knight_dict = knights["red_knight"]

    lancelot = knight_dict_create(lancelot_dict)
    arthur = knight_dict_create(arthur_dict)
    mordred = knight_dict_create(mordred_dict)
    red_knight = knight_dict_create(red_knight_dict)

    lancelot = Warrior(lancelot)
    arthur = Warrior(arthur)
    mordred = Warrior(mordred)
    red_knight = Warrior(red_knight)

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
