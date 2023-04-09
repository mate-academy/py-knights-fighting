from app.knigts import Knight

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
        "name": "Artur",
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


def battle(knights: dict) -> dict:
    list_of_knights = []
    for knight_name, value in knights.items():
        list_of_knights.append(
            Knight(
                value.get("name"),
                value.get("power"),
                value.get("hp")
            )
        )
    # preparations
    for i, knight in enumerate(knights):
        list_of_knights[i].apply_potion(knights.get(knight).get("potion"))
        list_of_knights[i].apply_armour(knights.get(knight).get("armour"))
        list_of_knights[i].apply_weapon(knights.get(knight).get("weapon"))

    # Battle

    for i in range(len(list_of_knights) // 2):
        list_of_knights[i].hp -= (
            list_of_knights[i + 2].power - list_of_knights[i].protection
        )
        list_of_knights[i + 2].hp -= (
            list_of_knights[i].power - list_of_knights[i + 2].protection
        )
        if list_of_knights[i].hp <= 0:
            list_of_knights[i].hp = 0
        if list_of_knights[i + 2].hp <= 0:
            list_of_knights[i + 2].hp = 0
    # return battle results
    return {
        list_of_knights[i].name: list_of_knights[i].hp
        for i in range(len(list_of_knights))
    }
