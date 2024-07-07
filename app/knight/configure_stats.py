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


def get_config(knights_config: dict, knight_name: str) -> dict:
    return knights_config[knight_name]


def apply_armor(knight_config: dict) -> None:
    knight_config["protection"] = 0
    for armor in knight_config["armour"]:
        knight_config["protection"] += armor["protection"]


def apply_weapon(knight_config: dict) -> None:
    knight_config["power"] += knight_config["weapon"]["power"]


def apply_potion(knight_config: dict) -> None:
    if knight_config["potion"] is not None:
        if "power" in knight_config["potion"]["effect"]:
            knight_config["power"] \
                += knight_config["potion"]["effect"]["power"]

        if "protection" in knight_config["potion"]["effect"]:
            knight_config["protection"] \
                += knight_config["potion"]["effect"]["protection"]

        if "hp" in knight_config["potion"]["effect"]:
            knight_config["hp"] \
                += knight_config["potion"]["effect"]["hp"]
