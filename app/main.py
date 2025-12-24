from app.battle import Battle
from app.knight.armour import Armour
from app.knight.knight import Knight
from app.knight.potion import Potion
from app.knight.weapon import Weapon

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


def create_knight_by_config(config: dict) -> Knight:
    knight = Knight(
        name=config["name"],
        power=config["power"],
        hp=config["hp"]
    )
    knight.armours = [
        Armour(part=armor["part"], protection=armor["protection"])
        for armor in config["armour"]
    ]
    knight.weapon = Weapon(
        name=config["weapon"]["name"],
        power=config["weapon"]["power"]
    )
    if config["potion"] is not None:
        potion_effects = {
            name: value
            for name, value in config["potion"]["effect"].items()
        }
        knight.potion = Potion(
            name=config["potion"]["name"],
            hp=potion_effects.get("hp"),
            power=potion_effects.get("power"),
            protection=potion_effects.get("protection")
        )

    return knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = create_knight_by_config(knights_config["lancelot"])
    # arthur
    arthur = create_knight_by_config(knights_config["arthur"])
    # mordred
    red_knight = create_knight_by_config(knights_config["red_knight"])
    # mordred
    mordred = create_knight_by_config(knights_config["mordred"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    fight_pairs = [
        # 1 Lancelot vs Mordred:
        (lancelot, mordred),
        # 2 Arthur vs Red Knight:
        (arthur, red_knight)
    ]

    for knight in fight_pairs:
        Battle.fight(*knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
