from app.player import Knight
from app.player.knight_name import KnightName
from app.player.knight_attribute import KnightAttribute

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


def battle(knights: dict) -> dict:
    players = create_players(knights)
    players[KnightName.LANCELOT.value].duel(players[KnightName.MORDRED.value])
    players[KnightName.ARTHUR.value].duel(players[KnightName.RED_KNIGHT.value])

    knights_names = [KnightName.LANCELOT.value,
                     KnightName.ARTHUR.value,
                     KnightName.MORDRED.value,
                     KnightName.RED_KNIGHT.value]

    result = {}
    for knight in knights_names:
        result[players[knight].name] = players[knight].hp
    return result


def create_players(knights: dict) -> dict:
    players = {}
    for knight in knights.values():
        players[knight[KnightAttribute.NAME.value]] = (
            Knight(
                knight[KnightAttribute.NAME.value],
                knight[KnightAttribute.POWER.value],
                knight[KnightAttribute.HP.value],
                knight[KnightAttribute.ARMOUR.value],
                knight[KnightAttribute.WEAPON.value]
                [KnightAttribute.POWER.value],
            )
        )
        players[knight[KnightAttribute.NAME.value]]\
            .apply_potion(knight[KnightAttribute.POTION.value])
    return players


print(battle(KNIGHTS))
