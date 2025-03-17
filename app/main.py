from __future__ import annotations


from app.battle import Knight

knights = {
    "lancelot": {
        "name": "Lancelot",
        "power": 85,
        "hp": 150,
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
    knight_list = []
    for knight_name, data in knights_config.items():
        knight = Knight(data["name"], data["power"], data["hp"])
        knight.power += data["weapon"]["power"]
        if data["potion"] is not None:
            if "power" in data["potion"]["effect"]:
                knight.power += data["potion"]["effect"]["power"]

            if "protection" in data["potion"]["effect"]:
                knight.protection += data["potion"]["effect"]["protection"]

            if "hp" in data["potion"]["effect"]:
                knight.hp += data["potion"]["effect"]["hp"]
        for i in data["armour"]:
            knight.protection += i["protection"]
        knight_list.append(knight)
    for knight in knight_list:
        if knight.name == "Lancelot":
            lancelot = knight
        if knight.name == "Arthur":
            arthur = knight
        if knight.name == "Mordred":
            mordred = knight
        if knight.name == "Red Knight":
            red_knight = knight

    lancelot.knight_battle(other=mordred)
    arthur.knight_battle(other=red_knight)

    return {lancelot.name: lancelot.hp, arthur.name: arthur.hp,
            mordred.name: mordred.hp, red_knight.name: red_knight.hp}


knights = battle(knights)
