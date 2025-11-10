from __future__ import annotations

from app.combatants import Knight

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


def apply_armour(knight: Knight) -> None:
    knight.protection = 0
    for armour in knight.armour:
        knight.protection += armour["protection"]


def apply_weapon(knight: Knight) -> None:
    knight.power += knight.weapon["power"]


def apply_potion(knight: Knight) -> None:
    if knight.potion is not None:
        if "power" in knight.potion["effect"]:
            knight.power += knight.potion["effect"]["power"]
        if "protection" in knight.potion["effect"]:
            knight.protection += knight.potion["effect"]["protection"]
        if "hp" in knight.potion["effect"]:
            knight.hp += knight.potion["effect"]["hp"]


def fight_battle(knight: Knight, knight2: Knight) -> None:
    knight.hp -= knight2.power - knight.protection
    knight2.hp -= knight.power - knight2.protection

    # check if someone fell in battle
    if knight.hp <= 0:
        knight.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config: dict) -> dict:

    # MAKE CLASSES
    for knight_name, knight in knights_config.items():
        Knight.knights_list.update({
            knight_name:
                Knight(
                    name=knight["name"],
                    power=knight["power"],
                    hp=knight["hp"],
                    armour=knight["armour"],
                    weapon=knight["weapon"],
                    potion=knight["potion"]
                )
        })

    # BATTLE PREPARATIONS:

    dict_of_knights_to_battle = {}
    # lancelot
    dict_of_knights_to_battle.update({
        "lancelot": Knight.knights_list["lancelot"]
    })
    # arthur
    dict_of_knights_to_battle.update({
        "arthur": Knight.knights_list["arthur"]
    })
    # mordred
    dict_of_knights_to_battle.update({
        "mordred": Knight.knights_list["mordred"]
    })
    # red_knight
    dict_of_knights_to_battle.update({
        "red_knight": Knight.knights_list["red_knight"]
    })

    for knight in dict_of_knights_to_battle.values():
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight_battle(
        dict_of_knights_to_battle["lancelot"],
        dict_of_knights_to_battle["mordred"]
    )
    # 2 Arthur vs Red Knight:
    fight_battle(
        dict_of_knights_to_battle["arthur"],
        dict_of_knights_to_battle["red_knight"]
    )

    # Return battle results:
    return {
        dict_of_knights_to_battle["lancelot"].name:
            dict_of_knights_to_battle["lancelot"].hp,
        dict_of_knights_to_battle["arthur"].name:
            dict_of_knights_to_battle["arthur"].hp,
        dict_of_knights_to_battle["mordred"].name:
            dict_of_knights_to_battle["mordred"].hp,
        dict_of_knights_to_battle["red_knight"].name:
            dict_of_knights_to_battle["red_knight"].hp,
    }


# print(battle(KNIGHTS))
# {'Lancelot': 0, 'Arthur': 30, 'Mordred': 35, 'Red Knight': 5}
