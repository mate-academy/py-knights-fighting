from app.knights import Knight, fight

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


def create_knights(knights: dict) -> dict:
    knight_instances = {}

    for knight_name, knight_value in knights.items():
        knight_instance = Knight(
            name=knight_value["name"],
            power=knight_value["power"],
            hp=knight_value["hp"],
            armour=knight_value["armour"],
            weapon=knight_value["weapon"],
            potion=knight_value["potion"],
        )
        knight_instances[knight_name] = knight_instance
    return knight_instances


def apply_preparation(knight_instances: dict) -> None:
    for knight_name, knight_instance in knight_instances.items():
        knight_instance.preparation()


def battle(knight_instances: dict) -> dict:
    lancelot = knight_instances["lancelot"]
    arthur = knight_instances["arthur"]
    mordred = knight_instances["mordred"]
    red_knight = knight_instances["red_knight"]

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


knight_instances = create_knights(KNIGHTS)

apply_preparation(knight_instances)

battle_result_hp = battle(knight_instances)

print(battle_result_hp)
