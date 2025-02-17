from typing import List, Dict

from app.armour import Armour
from app.knight import Knight
from app.potion import Potion
from app.weapon import Weapon

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
    create_knights(knightsConfig)

    lancelot = Knight.knights.get("Lancelot")
    mordred = Knight.knights.get("Mordred")
    arthur = Knight.knights.get("Arthur")
    red_knight = Knight.knights.get("Red Knight")

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


def armour_knight(knight: Knight, armours_params: List[dict]) -> None:
    for armour_params in armours_params:
        armour = Armour(
            part=armour_params.get("part"),
            protection=armour_params.get("protection"),
        )
        knight.armour(armour)


def weapon_knight(knight: Knight, weapon_params: dict) -> None:
    weapon = Weapon(
        name=weapon_params.get("name"),
        power=weapon_params.get("power"),
    )
    knight.weapon(weapon)


def potion_knight(knight: Knight, potion_params: dict) -> None:
    potion = Potion(
        name=potion_params.get("name"),
        power=potion_params.get("effect").get("power"),
        hp=potion_params.get("effect").get("hp"),
        protection=potion_params.get("effect").get("protection"),
    )
    knight.potion(potion)


def create_knights(config: Dict[str, dict]) -> None:
    knights = config.values()

    for params in knights:
        knight = Knight(
            name=params.get("name"),
            power=params.get("power"),
            hp=params.get("hp"),
        )

        if params.get("armour"):
            armour_knight(knight, params.get("armour"))
        if params.get("weapon"):
            weapon_knight(knight, params.get("weapon"))
        if params.get("potion"):
            potion_knight(knight, params.get("potion"))


def fight(knight_a: Knight, knight_b: Knight) -> None:
    knight_a.fight(knight_b.power)
    knight_b.fight(knight_a.power)


print(battle(KNIGHTS))
