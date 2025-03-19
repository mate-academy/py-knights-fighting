from app.battle.pair_knights import PairKnights
from app.knights.knight_power import Power
from app.knights.knight_protection import Protection
from app.knights.knight_hp import Hp


class KnightsConfig:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 protection: int,
                 weapon_power: int,
                 potion: dict,
                 effect: dict,
                 effect_power: int,
                 effect_protection: int,
                 effect_hp: int
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.protection = protection
        self.weapon_power = weapon_power
        self.potion = potion
        self.effect = effect
        self.effect_power = effect_power
        self.effect_protection = effect_protection
        self.effect_hp = effect_hp


knights = {
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
    }, }


def battle(knights: dict) -> dict:
    result = {}
    knight_list = []
    for knight in list(knights.keys()):
        if knights[knight]["potion"] is not None:
            knight = KnightsConfig(name=knights[knight]["name"],
                                   power=knights[knight]["power"],
                                   hp=knights[knight]["hp"],
                                   armour=knights[knight]["armour"],
                                   protection=0,
                                   weapon_power=knights[knight]["weapon"]
                                   ["power"],
                                   potion=knights[knight]["potion"],
                                   effect=knights[knight]["potion"]["effect"],
                                   effect_power=knights[knight]
                                   ["potion"]["effect"].get("power", 0),
                                   effect_protection=knights[knight]
                                   ["potion"]["effect"].get("protection", 0),
                                   effect_hp=knights[knight]
                                   ["potion"]["effect"].get("hp", 0)
                                   )
        else:
            knight = KnightsConfig(name=knights[knight]["name"]
                                   , power=knights[knight]["power"]
                                   , hp=knights[knight]["hp"]
                                   , armour=knights[knight]["armour"]
                                   , protection=0
                                   , weapon_power=knights[knight]
                                   ["weapon"]["power"]
                                   , potion={}
                                   , effect={}
                                   , effect_power=0
                                   , effect_protection=0
                                   , effect_hp=0)
        knight_list.append(knight)

    # BATTLE PREPARATIONS:
    for knight in knight_list:
        knight.power = Power.knight_power(power=knight.power,
                                          weapon_power=knight.weapon_power,
                                          effect_power=knight.effect_power)
        knight.protection = (Protection.knight_protection
                             (knight_armour=knight.armour,
                              protection=knight.protection,
                              effect_protection=knight.effect_protection))
        knight.hp = Hp.knight_hp(hp=knight.hp, effect_hp=knight.effect_hp)

    PairKnights.battle_pair_result(knight_list[0], knight_list[2])
    PairKnights.battle_pair_result(knight_list[1], knight_list[3])
    result[knight_list[0].name] = knight_list[0].hp
    result[knight_list[1].name] = knight_list[1].hp
    result[knight_list[2].name] = knight_list[2].hp
    result[knight_list[3].name] = knight_list[3].hp
    return result
