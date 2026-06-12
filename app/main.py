from app.pkg.armour import Armour
from app.pkg.battle import Battle
from app.pkg.knight import Knight
from app.pkg.potion import Potion
from app.pkg.weapon import Weapon

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


def parse_knights_config(knights_config: dict, *args: str) -> list[Knight]:
    knights = []

    for knight in args:
        knight_data = knights_config[knight]

        knight = Knight(
            knight_data["name"],
            knight_data["power"],
            knight_data["hp"]
        )

        knight.weapon = Weapon(
            knight_data["weapon"]["name"],
            knight_data["weapon"]["power"]
        )

        knight.armour = [
            Armour(armour["part"], armour["protection"])
            for armour in knight_data["armour"]
        ]

        if knight_data["potion"] is not None:
            knight.potion = Potion(
                knight_data["potion"]["name"],
                knight_data["potion"]["effect"]
            )
        knights.append(knight)
    return knights


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    lancelot, arthur, mordred, red_knight = parse_knights_config(
        knights_config,
        "lancelot",
        "arthur",
        "mordred",
        "red_knight"
    )

    lancelot = Battle.gear_check(lancelot)
    arthur = Battle.gear_check(arthur)
    mordred = Battle.gear_check(mordred)
    red_knight = Battle.gear_check(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot, mordred = Battle.fight(lancelot, mordred)

    # check if someone fell in battle
    lancelot.hp = Battle.check_hp(lancelot.hp)
    mordred.hp = Battle.check_hp(mordred.hp)

    # 2 Arthur vs Red Knight:
    arthur, red_knight = Battle.fight(arthur, red_knight)

    # check if someone fell in battle
    arthur.hp = Battle.check_hp(arthur.hp)
    red_knight.hp = Battle.check_hp(red_knight.hp)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
