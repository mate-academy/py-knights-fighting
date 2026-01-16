from app.knight.knight import Knight
from app.knight.hp_protection_and_power.hp_and_protection import HP
from app.knight.hp_protection_and_power.power import Power


knights_stats_before_battle = {
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


def battle(knights_stats_before_battle: dict) -> dict:

    knights = {}

    for knight_name, knight_stats in knights_stats_before_battle.items():
        knights[knight_name] = Knight(knight_stats)

    for knight in knights:
        knights[knight].hp = HP.total_hp_before_battle(knights[knight])
        knights[knight].power = Power.total_power(knights[knight])

    # 1 Lancelot vs Mordred:
    knights["lancelot"].hp -= knights["mordred"].power
    knights["mordred"].hp -= knights["lancelot"].power

    # 2 Arthur vs Red Knight:
    knights["arthur"].hp -= knights["red_knight"].power
    knights["red_knight"].hp -= knights["arthur"].power

    for knight in knights:
        knights[knight].check_hp_after_battle()

    return {knights[knight].name: knights[knight].hp for knight in knights}


if __name__ == "__main__":
    print(battle(knights_stats_before_battle))
