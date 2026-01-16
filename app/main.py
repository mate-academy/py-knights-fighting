from app.knights.knight_class import Knight

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
knights_info = KNIGHTS


def battle(knights_info: dict) -> dict:
    basic_knights_info = []
    knights_classified = []
    knights_stats_updated = []

    for attribute, attribute_value in knights_info.items():
        basic_knights_info.append(knights_info[attribute])

    for attribute in basic_knights_info:
        knight = Knight(
            attribute["name"],
            attribute["power"],
            attribute["hp"],
            attribute["armour"],
            attribute["weapon"],
            attribute["potion"],
        )
        knights_classified.append(knight)

    for knight in knights_classified:
        knight.__class__.knight_ready_for_fight(knight)
        knights_stats_updated.append(knight)

    knight_1 = knights_stats_updated[0]
    knight_2 = knights_stats_updated[2]
    knight_3 = knights_stats_updated[1]
    knight_4 = knights_stats_updated[3]

    knights_list = [knight_1, knight_2, knight_3, knight_4]
    battle_pairs = [[knight_1, knight_2], [knight_3, knight_4]]

    for pair in battle_pairs:
        pair[0].hp -= pair[1].power - pair[0].protection
        pair[1].hp -= pair[0].power - pair[1].protection

    for knight in knights_list:
        if knight.hp <= 0:
            knight.hp = 0

    for pair in battle_pairs:

        print(f" xxx BATTLE {pair[0].name} & {pair[1].name}  xxx ")

        if pair[0].hp == 0 and pair[1].hp != 0:
            print(f"{pair[0].name} defeated.")
            print(f"{pair[1].name} win!")
        if pair[1].hp == 0 and pair[0].hp != 0:
            print(f"{pair[1].name} defeated.")
            print(f"{pair[0].name} win!")
        if pair[0].hp != 0 and pair[1].hp != 0:
            print('"Happy End", no one is defeated.')

    return {
        knight_1.name: knight_1.hp,
        knight_3.name: knight_3.hp,
        knight_2.name: knight_2.hp,
        knight_4.name: knight_4.hp,
    }


battle(knights_info)
