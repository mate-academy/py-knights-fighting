from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.potion import Potion
from app.knights.weapon import Weapon
from app.knights.effect import Effect
from app.battle.actions import single_battle


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


def create_knight(data: dict) -> Knight:
    name = data["name"]
    power = data["power"]
    hp = data["hp"]
    armour = [
        Armour(part=a["part"], protection=a["protection"])
        for a in data.get("armour", [])
    ]
    weapon = Weapon(name=data["weapon"]["name"], power=data["weapon"]["power"])

    potion_data = data.get("potion")
    potion = None
    if potion_data:
        effect_data = potion_data["effect"]
        effect = Effect(
            power=effect_data.get("power", 0),
            hp=effect_data.get("hp", 0),
            protection=effect_data.get("protection", 0)
        )
        potion = Potion(name=potion_data["name"], effect=effect)

    knight = Knight(
        name=name,
        power=power,
        hp=hp,
        armour=armour,
        weapon=weapon,
        potion=potion
    )

    knight.power += weapon.power

    if potion:
        potion.effect.apply_effect(knight)
    return knight


def battle(knights_config: dict) -> dict:
    lancelot = create_knight(knights_config["lancelot"])
    mordred = create_knight(knights_config["mordred"])
    arthur = create_knight(knights_config["arthur"])
    red_knight = create_knight(knights_config["red_knight"])

    result1 = single_battle(lancelot, mordred)
    result2 = single_battle(arthur, red_knight)

    return {
        **result1,
        **result2,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
