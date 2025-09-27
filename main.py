from app.knight.knight import Knight
from app.battle.battle import Battle
from app.knight.armour import Armour
from app.knight.weapon import Weapon
from app.knight.potion import Potion


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


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(
        name=knightsConfig["lancelot"]["name"],
        power=knightsConfig["lancelot"]["power"],
        hp=knightsConfig["lancelot"]["hp"],
        armour=[
            Armour(
                part=armour["part"],
                protection=armour["protection"]
            )
            for armour in knightsConfig["lancelot"]["armour"]
        ],
        weapon=Weapon(
            name=knightsConfig["lancelot"]["weapon"]["name"],
            power=knightsConfig["lancelot"]["weapon"]["power"]
        ),
        potion=
        Potion(
            name=knightsConfig["lancelot"]["potion"]["name"],
            effect=knightsConfig["lancelot"]["potion"]["effect"]
        )
        if knightsConfig["lancelot"]["potion"]
        else None
    )
    #Calculate stats
    lancelot.calculate_stats()

    # arthur
    arthur = Knight(
        name=knightsConfig["arthur"]["name"],
        power=knightsConfig["arthur"]["power"],
        hp=knightsConfig["arthur"]["hp"],
        armour=[
            Armour(
            part=armour["part"],
            protection=armour["protection"]
            )
            for armour in knightsConfig["arthur"]["armour"]
        ],
        weapon=Weapon(
            name=knightsConfig["arthur"]["weapon"]["name"],
            power=knightsConfig["arthur"]["weapon"]["power"]
        ),
        potion=
        Potion(
            name=knightsConfig["arthur"]["potion"]["name"],
            effect=knightsConfig["arthur"]["potion"]["effect"]
        )
        if knightsConfig["arthur"]["potion"]
        else None
    )
    # Calculate stats
    arthur.calculate_stats()

    # mordred
    mordred = Knight(
        name=knightsConfig["mordred"]["name"],
        power=knightsConfig["mordred"]["power"],
        hp=knightsConfig["mordred"]["hp"],
        armour=[
            Armour(
                part=armour["part"],
                protection=armour["protection"]
            )
            for armour in knightsConfig["mordred"]["armour"]
        ],
        weapon=Weapon(
            name=knightsConfig["mordred"]["weapon"]["name"],
            power=knightsConfig["mordred"]["weapon"]["power"]
        ),
        potion=
        Potion(
            name=knightsConfig["mordred"]["potion"]["name"],
            effect=knightsConfig["mordred"]["potion"]["effect"]
        )
        if knightsConfig["mordred"]["potion"]
        else None
    )
    # Calculate stats
    mordred.calculate_stats()

    # red_knight
    red_knight = Knight(
        name=knightsConfig["red_knight"]["name"],
        power=knightsConfig["red_knight"]["power"],
        hp=knightsConfig["red_knight"]["hp"],
        armour=[
            Armour(
                part=armour["part"],
                protection=armour["protection"]
            )
            for armour in knightsConfig["red_knight"]["armour"]
        ],
        weapon=Weapon(
            name=knightsConfig["red_knight"]["weapon"]["name"],
            power=knightsConfig["red_knight"]["weapon"]["power"]
        ),
        potion=
        Potion(
            name=knightsConfig["red_knight"]["potion"]["name"],
            effect=knightsConfig["red_knight"]["potion"]["effect"]
        )
        if knightsConfig["red_knight"]["potion"]
        else None
    )
    # Calculate stats
    red_knight.calculate_stats()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle.battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    Battle.battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
