from app.knight import Knight
from app.battle import battle_from_objects


lancelot = Knight(
    name="Lancelot",
    power=35,
    hp=100,
    armour=[],
    weapon={"name": "Metal Sword", "power": 50},
    potion=None
)

arthur = Knight(
    name="Arthur",
    power=45,
    hp=75,
    armour=[
        {"part": "helmet", "protection": 15},
        {"part": "breastplate", "protection": 20},
        {"part": "boots", "protection": 10}
    ],
    weapon={"name": "Two-handed Sword", "power": 55},
    potion=None
)

mordred = Knight(
    name="Mordred",
    power=30,
    hp=90,
    armour=[
        {"part": "breastplate", "protection": 15},
        {"part": "boots", "protection": 10}
    ],
    weapon={"name": "Poisoned Sword", "power": 60},
    potion={
        "name": "Berserk",
        "effect": {
            "power": 15,
            "hp": -5,
            "protection": 10
        }
    }
)

red_knight = Knight(
    name="Red Knight",
    power=40,
    hp=70,
    armour=[
        {"part": "breastplate", "protection": 25}
    ],
    weapon={"name": "Sword", "power": 45},
    potion={
        "name": "Blessing",
        "effect": {
            "hp": 10,
            "power": 5
        }
    }
)
my_knights = {
    "lancelot": lancelot,
    "arthur": arthur,
    "mordred": mordred,
    "red_knight": red_knight
}


def run_battle_for_demo(knights: dict) -> dict:
    result = battle_from_objects(knights)

    return result


print(run_battle_for_demo(my_knights))
