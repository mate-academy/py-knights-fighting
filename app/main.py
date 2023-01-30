from app.player import Knight
from app.player import KnightObj
from app.player import PlayersName as Pn

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
    players[Pn.LANCELOT].duel(players[Pn.MORDRED])
    players[Pn.ARTHUR].duel(players[Pn.RED_KNIGHT])

    return {
        players[Pn.LANCELOT].name: players[Pn.LANCELOT].hp,
        players[Pn.ARTHUR].name: players[Pn.ARTHUR].hp,
        players[Pn.MORDRED].name: players[Pn.MORDRED].hp,
        players[Pn.RED_KNIGHT].name: players[Pn.RED_KNIGHT].hp,
    }


def create_players(knights: dict) -> dict:
    players = {}
    knight_obj = KnightObj()
    for knight in knights.values():
        players[knight[knight_obj.NAME]] = \
            Knight(knight[knight_obj.NAME],
                   knight[knight_obj.POWER],
                   knight[knight_obj.HP],
                   knight[knight_obj.ARMOUR],
                   knight[knight_obj.WEAPON],
                   knight[knight_obj.POTION])
    return players


print(battle(KNIGHTS))
