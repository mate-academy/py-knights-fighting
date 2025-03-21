from app.total import Power


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


def battle(knights_config: dict) -> dict:
    def fight(knight1: str, knight2: str) -> None:
        knights_config[knight1]["hp"] -= max(
            0,
            knights_config[knight2]["power"]
            - knights_config[knight1]["protection"]
        )
        knights_config[knight2]["hp"] -= max(
            0,
            knights_config[knight1]["power"]
            - knights_config[knight2]["protection"]
        )

    def tot() -> dict:
        knight_names = list(knights_config.keys())

        for name in knight_names:
            knight_power = Power(
                armour=knights_config[name]["armour"],
                weapon=knights_config[name]["weapon"],
                potion=knights_config[name]["potion"]
            )

            sum_hp, sum_power, sum_protection = knight_power.total_power()

            knights_config[name]["hp"] += sum_hp
            knights_config[name]["power"] += sum_power
            knights_config[name]["protection"] = (
                knights_config[name].get("protection", 0) + sum_protection
            )

        fight(knight_names[0], knight_names[2])
        fight(knight_names[1], knight_names[3])

        return {
            name: max(0, knights_config[name]["hp"]) for name in knight_names
        }

    return tot()


print(battle(KNIGHTS))
