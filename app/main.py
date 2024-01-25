from app.items.weapon import Weapon
from app.items.potion import Potion
from app.items.armour import Armour
from app.participants.knight import Knight

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
    # lancelot
    lancelot = Knight(
        name=knights["lancelot"]["name"],
        power=knights["lancelot"]["power"],
        hp=knights["lancelot"]["hp"],
        armour=[
            Armour(part=armour["part"],
                   protection=armour["protection"])
            for armour in knights["lancelot"]["armour"]
        ],
        weapon=Weapon(name=knights["lancelot"]["weapon"]["name"],
                      power=knights["lancelot"]["weapon"]["power"]),
        potion=None if knights["lancelot"].get("potion") is None else
        Potion(name=knights["lancelot"]["potion"]["name"],
               effect=knights["lancelot"]["potion"]["effect"])
    )
    # arthur
    arthur = Knight(
        name=knights["arthur"]["name"],
        power=knights["arthur"]["power"],
        hp=knights["arthur"]["hp"],
        armour=[Armour(part=armour["part"],
                       protection=armour["protection"])
                for armour in knights["arthur"]["armour"]],
        weapon=Weapon(name=knights["arthur"]["weapon"]["name"],
                      power=knights["arthur"]["weapon"]["power"]),
        potion=None if knights["arthur"].get("potion") is None else
        Potion(name=knights["arthur"]["potion"]["name"],
               effect=knights["arthur"]["potion"]["effect"])
    )
    # mordred
    mordred = Knight(
        name=knights["mordred"]["name"],
        power=knights["mordred"]["power"],
        hp=knights["mordred"]["hp"],
        armour=[Armour(part=armour["part"],
                       protection=armour["protection"])
                for armour in knights["mordred"]["armour"]],
        weapon=Weapon(name=knights["mordred"]["weapon"]["name"],
                      power=knights["mordred"]["weapon"]["power"]),
        potion=None if knights["mordred"].get("potion") is None else
        Potion(name=knights["mordred"]["potion"]["name"],
               effect=knights["mordred"]["potion"]["effect"])
    )
    # red_knight
    red_knight = Knight(
        name=knights["red_knight"]["name"],
        power=knights["red_knight"]["power"],
        hp=knights["red_knight"]["hp"],
        armour=[Armour(part=armour["part"],
                       protection=armour["protection"])
                for armour in knights["red_knight"]["armour"]],
        weapon=Weapon(name=knights["red_knight"]["weapon"]["name"],
                      power=knights["red_knight"]["weapon"]["power"]),
        potion=None if knights["red_knight"].get("potion") is None else
        Potion(name=knights["red_knight"]["potion"]["name"],
               effect=knights["red_knight"]["potion"]["effect"])
    )
    # 1 Lancelot vs Mordred:
    lancelot - mordred

    # 2 Arthur vs Red Knight:
    arthur - red_knight

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
