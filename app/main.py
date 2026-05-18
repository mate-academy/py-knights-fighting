from app.ammo.armour import Armour
from app.ammo.potion import Potion
from app.ammo.weapon import Weapon
from app.battle import knights_fight
from app.knights import Knight


def create_knight(name: str, data: dict) -> Knight:
    armour = Armour(data["armour"])
    weapon = Weapon(
        data["weapon"]["name"],
        data["weapon"]["power"]
    )

    potion = None

    if data["potion"] is not None:
        effect = data["potion"]["effect"]
        potion = Potion(
            effect.get("hp"),
            effect.get("power"),
            effect.get("protection")
        )

    return Knight(
        name,
        data["power"],
        data["hp"],
        armour,
        weapon,
        potion
    )


knights = {
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


def battle(knights: dict) -> dict:
    lancelot = create_knight("Lancelot", knights["lancelot"])
    mordred = create_knight("Mordred", knights["mordred"])

    arthur = create_knight("Arthur", knights["arthur"])
    red_knight = create_knight("Red Knight", knights["red_knight"])

    first_fight = knights_fight(lancelot, mordred)
    second_fight = knights_fight(arthur, red_knight)

    return first_fight | second_fight


print(battle(knights))
