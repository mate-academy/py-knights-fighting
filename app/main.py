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
    all_knights = dict()
    for knight in knights_config:
        temp_knight = Knight(
            name=knights_config[knight]["name"],
            power=knights_config[knight]["power"],
            hp=knights_config[knight]["hp"]
        )
        for armour in knights_config[knight]["armour"]:
            temp_knight.set_armour(Armour(
                armour["part"],
                protection=armour["protection"]
            ))
        temp_knight.set_weapon(Weapon(
            knights_config[knight]["weapon"]["name"],
            power=knights_config[knight]["weapon"]["power"]
        ))
        if knights_config[knight]["potion"]:
            potion_property = knights_config[knight]["potion"]["effect"]
            for effect in potion_property:
                temp_power = (
                    potion_property["power"] if (
                        "power" in potion_property
                    ) else 0
                )
                temp_protection = (
                    potion_property["protection"] if (
                        "protection" in potion_property
                    ) else 0
                )
                temp_hp = (
                    potion_property["hp"] if (
                        "hp" in potion_property
                    ) else 0
                )
            temp_potion = Potion(
                name=knights_config[knight]["potion"]["name"],
                power=temp_power,
                protection=temp_protection,
                hp=temp_hp
            )
            temp_knight.set_potion(temp_potion)
        all_knights[knight] = temp_knight
    knights_fight(all_knights["lancelot"], all_knights["mordred"])
    knights_fight(all_knights["arthur"], all_knights["red_knight"])
    return {
        all_knights[knight].name: all_knights[knight].hp for (
            knight) in all_knights
    }


print(battle(KNIGHTS))
