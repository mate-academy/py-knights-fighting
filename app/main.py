from app.knight.knight import Knight

KNIGHTS = dict(lancelot={
    "name": "Lancelot",
    "power": 35,
    "hp": 100,
    "armour": [],
    "weapon": {
        "name": "Metal Sword",
        "power": 50,
    },
    "potion": None,
}, arthur={
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
}, mordred={
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
}, red_knight={
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
})


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        knight.apply_armour()
        knight.use_weapon()
        knight.drink_potion()

    lancelot.start_duel(mordred)
    arthur.start_duel(red_knight)

    return {
        lancelot.name: lancelot.stats["hp"],
        arthur.name: arthur.stats["hp"],
        mordred.name: mordred.stats["hp"],
        red_knight.name: red_knight.stats["hp"],
    }


print(battle(KNIGHTS))
