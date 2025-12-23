from app.knights.KnightsTemplate import KnightsTemplate


def battle(knights_list: dict) -> dict:
    fighters = {}
    for knight_name, knight_config in knights_list.items():
        instantiated_knight = KnightsTemplate(
            name=knight_config["name"],
            power=knight_config["power"],
            hp=knight_config["hp"],
            armour=knight_config["armour"],
            weapon=knight_config["weapon"],
            potion=knight_config["potion"],
            protection=knight_config.get("protection", 0)
        )

        fighters[knight_name] = instantiated_knight
    print(fighters)
    for knight in fighters.values():
        knight.add_power()
        knight.apply_potion()
        knight.add_protection()
    fighters["lancelot"].hp -= (fighters["mordred"].power
                                - fighters["lancelot"].protection)
    fighters["mordred"].hp -= (fighters["lancelot"].power
                               - fighters["mordred"].protection)
    if fighters["lancelot"].hp <= 0:
        fighters["lancelot"].hp = 0

    if fighters["mordred"].hp <= 0:
        fighters["mordred"].hp = 0
    fighters["arthur"].hp -= (fighters["red_knight"].power
                              - fighters["arthur"].protection)
    fighters["red_knight"].hp -= (fighters["arthur"].power
                                  - fighters["red_knight"].protection)
    if fighters["arthur"].hp <= 0:
        fighters["arthur"].hp = 0

    if fighters["red_knight"].hp <= 0:
        fighters["red_knight"].hp = 0
    return {
        fighters["lancelot"].name:
            fighters["lancelot"].hp,

        fighters["mordred"].name:
            fighters["mordred"].hp,

        fighters["arthur"].name:
            fighters["arthur"].hp,

        fighters["red_knight"].name:
            fighters["red_knight"].hp,
    }


knight_configs = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 75,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": {},
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
        },
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
        "potion": {},
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
            "power": 45,
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        },
    },
}

print(battle(knights_list=knight_configs))
