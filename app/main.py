from app.knights import Knight
from app.weapon import Weapon
from app.potions import Potion


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


def battle(knights_config: dict) -> dict:

    lancelot = Knight.create_knight(knights_config["lancelot"])
    arthur = Knight.create_knight(knights_config["arthur"])
    mordred = Knight.create_knight(knights_config["mordred"])
    red_knight = Knight.create_knight(knights_config["red_knight"])

    metal_sword = Weapon.create_weapon(knights_config["lancelot"]["weapon"])
    two_handed_sword = Weapon.create_weapon(knights_config["arthur"]["weapon"])
    poisoned_sword = Weapon.create_weapon(knights_config["mordred"]["weapon"])
    sword = Weapon.create_weapon(knights_config["red_knight"]["weapon"])

    lancelot.equip_weapon(metal_sword)
    arthur.equip_weapon(two_handed_sword)
    mordred.equip_weapon(poisoned_sword)
    red_knight.equip_weapon(sword)

    magic_power = Potion.create_potion(knights_config["lancelot"]["potion"])
    dragon_heart = Potion.create_potion(knights_config["arthur"]["potion"])
    berserk = Potion.create_potion(knights_config["mordred"]["potion"])
    blessing = Potion.create_potion(knights_config["red_knight"]["potion"])

    lancelot.drink_potion(magic_power)
    arthur.drink_potion(dragon_heart)
    mordred.drink_potion(berserk)
    red_knight.drink_potion(blessing)

    Knight.duel(lancelot, mordred)
    Knight.duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
