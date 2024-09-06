from app.heroes.knight import Knight
from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


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
    """
    Simulates a battle between knights and returns
    the remaining health points of each knight after the battle.

    Args:
        knights_config (dict):
            A dictionary containing the configuration of all knights,
            including their stats, armor, weapons, and potions.

    Returns:
        dict: A dictionary with knight names as keys
        and their remaining health points (hp) as values.
    """
    # BATTLE PREPARATIONS:
    knights = battle_prepare(knights_config)
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    # Return battle results:
    return {knight.name: knight.hp for knight in knights.values()}


def battle_prepare(knights_config: dict) -> dict[str, Knight]:
    """
    Prepares the knights for battle by applying
    armor, weapons, and potions to their stats.

    Args:
        knights_config (dict):
        A dictionary containing knight configurations,
        including their armor, weapons, and potions.

    Returns:
        dict[str, Knight]:
            A dictionary of prepared Knight objects ready for battle.
    """
    knights = {}
    for name, properties in knights_config.items():
        knight = create_knight(properties["name"], properties)
        if properties["armour"]:
            armours = [
                create_armour(armour) for armour in properties["armour"]
            ]
            knight.set_protection(armours)
        weapon = create_weapon(properties["weapon"])
        knight.increase_power(weapon)
        if properties["potion"]:
            potion = create_potion(properties["potion"])
            knight.set_effect(potion)
        knights[name] = knight

    return knights


def create_knight(name: str, propertires: dict) -> Knight:
    """
    Creates a Knight object based on the given properties.

    Args:
        name (str): The name of the knight.
        properties (dict):
            A dictionary containing the knight's base stats (hp, power, etc.).

    Returns:
        Knight: A new Knight object.
    """
    return Knight(name, propertires["power"], propertires["hp"])


def create_armour(armour: dict) -> Armour:
    """
    Creates an Armour object based on the given properties.

    Args:
        armour (dict):
            A dictionary containing the part of the armour
            and its protection value.

    Returns:
        Armour: A new Armour object.
    """
    return Armour(armour["part"], armour["protection"])


def create_weapon(weapon: dict) -> Weapon:
    """
    Creates a Weapon object based on the given properties.

    Args:
        weapon (dict): A dictionary containing the weapon's name and power.

    Returns:
        Weapon: A new Weapon object.
    """
    return Weapon(weapon["name"], weapon["power"])


def create_potion(potion: dict) -> Potion:
    """
    Creates a Potion object based on the given properties.

    Args:
        potion (dict):
            A dictionary containing the potion's name and its effects on stats.

    Returns:
        Potion: A new Potion object.
    """
    return Potion(potion["name"], potion["effect"])


print(battle(KNIGHTS))
