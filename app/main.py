from app.knights.knight import Knight
from app.knights.weapon import Weapon
from app.knights.potion import Potion


def battle(knights_config):
    knights = []

    for knight_config in knights_config.values():
        name = knight_config["name"]
        power = knight_config["power"]
        hp = knight_config["hp"]
        armour = knight_config["armour"]
        weapon = Weapon(knight_config["weapon"]["name"], knight_config["weapon"]["power"])
        potion_config = knight_config["potion"]
        potion = None

        if potion_config is not None:
            potion = Potion(potion_config["name"], potion_config["effect"])

        knight = Knight(name, power, hp, armour, weapon, potion)
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

        knights.append(knight)

    results = {}

    for knight in knights:
        remaining_knights = knights.copy()
        remaining_knights.remove(knight)

        for opponent in remaining_knights:
            knight_hp = max(knight.hp - opponent.power + knight.protection, 0)
            opponent_hp = max(opponent.hp - knight.power + opponent.protection, 0)

            results[knight.name] = knight_hp
            results[opponent.name] = opponent_hp

    return results


if __name__ == "__main__":
    KNIGHTS = {
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
            "hp": 90,
            "armour": [
                {"part": "breastplate", "protection": 15},
                {"part": "boots", "protection": 10},
            ],
            "weapon": {"name": "Poisoned Sword", "power": 60},
            "potion": {
                "name": "Berserk",
                "effect": {"power": 15, "hp": -5, "protection": 10},
            },
        },
        "red_knight": {
            "name": "Red Knight",
            "power": 40,
            "hp": 70,
            "armour": [{"part": "breastplate", "protection": 25}],
            "weapon": {"name": "Sword", "power": 45},
            "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
        },
    }

    battle_result = battle(KNIGHTS)
    print(battle_result)
