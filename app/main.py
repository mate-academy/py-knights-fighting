from app.battle.fight_knights import Battle
from app.items.equipment import Armour, Weapon, Potion
from app.knights.character import Knight


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


def create_knight(knight_data: dict) -> Knight:
    weapon = Weapon(
        name=knight_data["weapon"]["name"],
        power=knight_data["weapon"]["power"])

    armour = [Armour(name=part["part"], protection=part["protection"])
              for part in knight_data["armour"]]

    if knight_data["potion"] is not None:
        potion = Potion(
            name=knight_data["potion"]["name"],
            effect=knight_data["potion"]["effect"])
    else:
        potion = None

    return Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        armours=armour,
        weapon=weapon,
        potion=potion
    )


def battle(knights_config: dict) -> dict:
    knights = {}

    for key, knight_data in knights_config.items():
        knights[key] = create_knight(knight_data)

    for knight in knights.values():
        knight.prepare_for_battle()

    Battle(
        first_knight=knights["lancelot"],
        second_knight=knights["mordred"]
    ).battle()

    Battle(
        first_knight=knights["arthur"],
        second_knight=knights["red_knight"]
    ).battle()

    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
