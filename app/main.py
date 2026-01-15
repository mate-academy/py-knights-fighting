from app.Game import Game

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
            },
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
            },
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
            },
        },
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
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def battle(knightsconfig: dict) -> dict:
    knights = Game(knightsconfig)
    players = knights.create_knights(knightsconfig)

    players["lancelot"].hp -= (players["mordred"].power
                               - players["lancelot"].armour)
    players["mordred"].hp -= (players["lancelot"].power
                              - players["mordred"].armour)

    if players["lancelot"].hp <= 0:
        players["lancelot"].hp = 0

    if players["mordred"].hp <= 0:
        players["mordred"].hp = 0

    players["arthur"].hp -= (players["red_knight"].power
                             - players["arthur"].armour)
    players["red_knight"].hp -= (players["arthur"].power
                                 - players["red_knight"].armour)

    if players["arthur"].hp <= 0:
        players["arthur"].hp = 0

    if players["red_knight"].hp <= 0:
        players["red_knight"].hp = 0

    return {
        players["lancelot"].name: players["lancelot"].hp,
        players["mordred"].name: players["mordred"].hp,
        players["arthur"].name: players["arthur"].hp,
        players["red_knight"].name: players["red_knight"].hp,
    }


print(battle(KNIGHTS))
