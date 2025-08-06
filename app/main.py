
from app.models.knight import Knight
from app.models.weapon import Weapon
from app.models.armour import ArmourPart
from app.models.potion import Potion
from app.services.battle import battle


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 40,
        "hp": 120,
        "weapon": {"name": "Sword", "power": 25},
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "shield", "protection": 15}
        ],
        "potion": {"name": "Healing", "effect": {"hp": 30}}
    },
    "mordred": {
        "name": "Mordred",
        "power": 45,
        "hp": 110,
        "weapon": {"name": "Axe", "power": 30},
        "armour": [
            {"part": "helmet", "protection": 8},
            {"part": "shield", "protection": 12}
        ]
    },
    "arthur": {
        "name": "Arthur",
        "power": 50,
        "hp": 130,
        "weapon": {"name": "Excalibur", "power": 35},
        "armour": [
            {"part": "helmet", "protection": 12},
            {"part": "shield", "protection": 18}
        ],
        "potion": {"name": "Strength", "effect": {"power": 20}}
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 42,
        "hp": 115,
        "weapon": {"name": "Mace", "power": 28},
        "armour": [
            {"part": "helmet", "protection": 9},
            {"part": "shield", "protection": 14}
        ]
    }
}


def create_knight_from_dict(data: dict) -> Knight:
    weapon_data = data.get("weapon")
    weapon = Weapon(**weapon_data) if weapon_data else None

    potion_data = data.get("potion")
    potion = None
    if potion_data:
        effect = potion_data["effect"]
        potion = Potion(potion_data["name"], effect)

    armour_data = data.get("armour", [])
    armour = [ArmourPart(part["part"],
                         part["protection"])
              for part in armour_data]

    return Knight(
        name=data["name"],
        base_power=data["power"],
        base_hp=data["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def main() -> None:
    lancelot = create_knight_from_dict(KNIGHTS["lancelot"])
    mordred = create_knight_from_dict(KNIGHTS["mordred"])
    arthur = create_knight_from_dict(KNIGHTS["arthur"])
    red_knight = create_knight_from_dict(KNIGHTS["red_knight"])

    result1 = battle(lancelot, mordred)
    result2 = battle(arthur, red_knight)

    print(result1)
    print(result2)


if __name__ == "__main__":
    main()
