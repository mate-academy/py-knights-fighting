from app.models.knight import Knight
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion
from app.models.battle import Battle

KNIGHTS = {
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "breastplate", "protection": 25},
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
    },
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 95,
        "armour": [
            {"part": "helmet", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Axe", "power": 40},
        "potion": {"name": "Poison", "effect": {"hp": -20}},
    },
}


def create_knight(data: dict) -> Knight:
    armour = [Armour(**a) for a in data.get("armour", [])]
    weapon = Weapon(**data["weapon"]) if data.get("weapon") else None
    potion = Potion(**data["potion"]) if data.get("potion") else None
    return Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def battle(knights_data: dict) -> dict:
    lancelot = create_knight(knights_data["lancelot"])
    mordred = create_knight(knights_data["mordred"])
    arthur = create_knight(knights_data["arthur"])
    red_knight = create_knight(knights_data["red_knight"])

    battle1 = Battle(lancelot, mordred)
    battle2 = Battle(arthur, red_knight)

    result1 = battle1.fight()
    result2 = battle2.fight()

    return {**result1, **result2}


if __name__ == "__main__":
    print(battle(KNIGHTS))
