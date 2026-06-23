from app.knight import Knight
from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion
from app.battle import Battle


def battle(knights: dict) -> dict:
    knights_dict = {}

    for keys, value in knights.items():
        name = value.get("name")
        power = value.get("power")
        hp = value.get("hp")
        armours = value.get("armour")
        weapon = value.get("weapon")
        potion = value.get("potion")

        knight = Knight(name, power, hp)
        knights_dict[keys] = knight

        if armours is not None:
            armours_obj = []
            for armour in armours:
                armours_obj.append(
                    Armour(armour.get("part"), armour.get("protection", 0))
                )
            knight.add_armour(armours_obj)

        if weapon is not None:
            knight.add_weapon(
                Weapon(weapon.get("name"), weapon.get("power", 0))
            )

        if potion is not None:
            knight.add_potion(Potion(potion.get("name"), potion.get("effect")))

    # Проводимо дуелі
    Battle(knights_dict["lancelot"], knights_dict["mordred"]).duel()
    Battle(knights_dict["arthur"], knights_dict["red_knight"]).duel()

    # {Ім'я_Лицаря: його_hp}
    return {
        knight.name: knight.hp
        for knight in knights_dict.values()
    }


if __name__ == "__main__":
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
                {"part": "helmet", "protection": 15},
                {"part": "breastplate", "protection": 20},
                {"part": "boots", "protection": 10}
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
                {"part": "breastplate", "protection": 15},
                {"part": "boots", "protection": 10}
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
                {"part": "breastplate", "protection": 25}
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

    print(battle(KNIGHTS))
