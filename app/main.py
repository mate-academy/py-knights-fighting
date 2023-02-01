from app.player import Knight
from app.player import consts

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
        "name": "Artur",
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
    players = create_players(knights)
    players[consts.LANCELOT].duel(players[consts.MORDRED])
    players[consts.ARTHUR].duel(players[consts.RED_KNIGHT])

    knights_names = [consts.LANCELOT,
                     consts.ARTHUR,
                     consts.MORDRED,
                     consts.RED_KNIGHT]

    result = {}
    for knight in knights_names:
        result[players[knight].name] = players[knight].hp
    return result


def create_players(knights: dict) -> dict:
    players = {}
    for knight in knights.values():
        players[knight[consts.NAME]] = (
            Knight(
                knight[consts.NAME],
                knight[consts.POWER],
                knight[consts.HP],
                knight[consts.ARMOUR],
                knight[consts.WEAPON][consts.POWER],
            )
        )
        players[knight[consts.NAME]].apply_potion(knight[consts.POTION])
    return players


print(battle(KNIGHTS))
