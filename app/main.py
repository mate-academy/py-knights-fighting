from app.pkg.Fighters import Fighters


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


def battle(knightsconfig: dict) -> Fighters:
    Fighters.list_fighters.clear()
    for name_fighter, dict_value in knightsconfig.items():
        name = dict_value["name"]
        hp = dict_value["hp"]
        power = dict_value["power"]
        protection = 0

        #  armour
        if dict_value["armour"]:
            for armour in dict_value["armour"]:
                protection += armour["protection"]

        #  weapon power
        weapon_power = dict_value["weapon"]["power"]
        power += weapon_power

        #  potion
        if dict_value["potion"]:
            if "power" in dict_value["potion"]["effect"]:
                power += dict_value["potion"]["effect"]["power"]
            if "protection" in dict_value["potion"]["effect"]:
                protection += dict_value["potion"]["effect"]["protection"]
            if "hp" in dict_value["potion"]["effect"]:
                hp += dict_value["potion"]["effect"]["hp"]

        #  added to class
        Fighters(name, hp, power, protection)

    return Fighters.battle_vs()
