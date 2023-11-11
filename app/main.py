from app.game_objects.knight import Knight
from app.game_objects.armour import Armour
from app.game_objects.weapon import Weapon
from app.game_objects.potion import Potion


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


def knights_fight(first: Knight, second: Knight) -> None:
    first.get_damage(second)
    second.get_damage(first)


def battle(knights_config: dict) -> dict:
    all_knights = []
    for knight in knights_config:
        temp_knight = Knight(
            name=knights_config[knight]["name"],
            power=knights_config[knight]["power"],
            hp=knights_config[knight]["hp"]
        )
        for i in range(len(knights_config[knight]["armour"])):
            temp_knight.set_armour(Armour(
                knights_config[knight]["armour"][i]["part"],
                protection=knights_config[knight]["armour"][i]["protection"]
            ))
        temp_knight.set_weapon(Weapon(
            knights_config[knight]["weapon"]["name"],
            power=knights_config[knight]["weapon"]["power"]
        ))
        if knights_config[knight]["potion"]:
            temp_potion = Potion(knights_config[knight]["potion"]["name"])
            if "power" in knights_config[knight]["potion"]["effect"]:
                temp_potion.power += (
                    knights_config[knight]["potion"]["effect"]["power"]
                )
            if "protection" in knights_config[knight]["potion"]["effect"]:
                temp_potion.protection += (
                    knights_config[knight]["potion"]["effect"]["protection"]
                )
            if "hp" in knights_config[knight]["potion"]["effect"]:
                temp_potion.hp += (
                    knights_config[knight]["potion"]["effect"]["hp"]
                )
            temp_knight.set_potion(temp_potion)
        all_knights.append(temp_knight)
    knights_fight(all_knights[0], all_knights[2])
    knights_fight(all_knights[1], all_knights[3])
    return {
        all_knights[i].name: all_knights[i].hp for i in range(len(KNIGHTS))
    }


print(battle(KNIGHTS))
