from app.battle import heroes_battle as battle_result
from app.stats_count import heroes_stats_count as stats_counter
from app.stats import Stats as stats

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


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knightsConfig["lancelot"]  # get all lancelot stats
    lancelot_prepare = stats_counter(
        lancelot
    )  # count lancelot stats for battle by app.stats_count.py
    lancelot_ready = stats(
        lancelot_prepare[0],
        lancelot_prepare[1],
        lancelot_prepare[2],
        lancelot_prepare[3],
    )  # objects of counted stats by app.stats.py

    # arthur
    arthur = knightsConfig["arthur"]  # get all arthur stats
    arthur_prepare = stats_counter(
        arthur
    )  # count arthur stats for battle by app.stats_count.py
    arthur_ready = stats(
        arthur_prepare[0],
        arthur_prepare[1],
        arthur_prepare[2],
        arthur_prepare[3]
    )  # objects of counted stats by app.stats.py

    # mordred
    mordred = knightsConfig["mordred"]  # get all mordred stats
    mordred_prepare = stats_counter(
        mordred
    )  # count mordred stats for battle by app.stats_count.py
    mordred_ready = stats(
        mordred_prepare[0],
        mordred_prepare[1],
        mordred_prepare[2],
        mordred_prepare[3]
    )  # objects of counted stats by app.stats.py

    # red_knight
    red_knight = knightsConfig[
        "red_knight"
    ]  # get all red_knight stats
    red_knight_prepare = stats_counter(
        red_knight
    )  # count red_knight stats for battle by app.stats_count.py
    red_knight_ready = stats(
        red_knight_prepare[0],
        red_knight_prepare[1],
        red_knight_prepare[2],
        red_knight_prepare[3],
    )  # objects of counted stats by app.stats.py

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    first_battle = battle_result(
        lancelot_ready, mordred_ready
    )  # count battle hero vs hero by app.battle

    # 2 Arthur vs Red Knight:
    second_battle = battle_result(
        arthur_ready, red_knight_ready
    )  # count battle hero vs hero by app.battle

    # Return battle results:
    return first_battle | second_battle


print(battle(KNIGHTS))
