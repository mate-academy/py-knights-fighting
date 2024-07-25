from app.equipment_data.red_knight_data import RedKnightData
from app.god.god import God
from app.human.knight import Knight
from app.battle.battle import Battle
from app.equipment_data.arthur_data import ArthurData
from app.equipment_data.lancelot_data import LancelotData
from app.equipment_data.mordred_data import MordredData

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
    ArthurData.set_data(knightsConfig["arthur"]["armour"], knightsConfig["arthur"]["weapon"])
    LancelotData.set_data(knightsConfig["lancelot"]["armour"], knightsConfig["lancelot"]["weapon"])
    MordredData.set_data(knightsConfig["mordred"]["armour"], knightsConfig["mordred"]["weapon"])
    RedKnightData.set_data(knightsConfig["red_knight"]["armour"], knightsConfig["red_knight"]["weapon"])

    l_squire = God.arise_servant("Lancelot's_squire")
    a_squire = God.arise_servant("arthur's_squire")
    m_squire = God.arise_servant("mordred's_squire")
    r_squire = God.arise_servant("red_knight's_squire")

    lancelot = Knight("Lancelot", knightsConfig["lancelot"]["power"], knightsConfig["lancelot"]["hp"])
    arthur = Knight("arthur", knightsConfig["arthur"]["power"], knightsConfig["arthur"]["hp"])
    mordred = Knight("mordred", knightsConfig["mordred"]["power"], knightsConfig["mordred"]["hp"])
    red_knight = Knight("red_knight", knightsConfig["red_knight"]["power"], knightsConfig["red_knight"]["hp"])

    lancelot.squire = l_squire
    arthur.squire = a_squire
    mordred.squire = m_squire
    red_knight.squire = r_squire

    l_squire.set_my_lord(lancelot)
    a_squire.set_my_lord(arthur)
    m_squire.set_my_lord(mordred)
    r_squire.set_my_lord(red_knight)

    lancelot.apply_armour()
    lancelot.apply_weapon()
    lancelot.apply_potion()

    arthur.apply_armour()
    arthur.apply_weapon()
    arthur.apply_potion()

    mordred.apply_armour()
    mordred.apply_weapon()
    mordred.apply_potion()

    red_knight.apply_armour()
    red_knight.apply_weapon()
    red_knight.apply_potion()
    Battle.lancelot_vs_mordred(lancelot, mordred)
    Battle.lancelot_vs_mordred(arthur, red_knight)

battle(KNIGHTS)
