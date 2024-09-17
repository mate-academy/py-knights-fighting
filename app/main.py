from app.knights.stats import Knight
from app.knights.battle import battle

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 60,
        "hp": 100,
        "armour": [{"part": "helmet", "protection": 20}],
        "weapon": {"name": "Spear", "power": 50},
        "potion": {"name": "Strength",
                   "effect": {"hp": 0, "power": 10, "protection": 5}},
    },
    "arthur": {
        "name": "Arthur",
        "power": 55,
        "hp": 90,
        "armour": [{"part": "shield", "protection": 30}],
        "weapon": {"name": "Excalibur", "power": 60},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 65,
        "hp": 110,
        "armour": [{"part": "plate", "protection": 25}],
        "weapon": {"name": "Axe", "power": 55},
        "potion": None,
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing",
                   "effect": {"hp": 10, "power": 5, "protection": 0}},
    }
}


def main() -> None:
    lancelot = Knight(**KNIGHTS["lancelot"])
    mordred = Knight(**KNIGHTS["mordred"])
    arthur = Knight(**KNIGHTS["arthur"])
    red_knight = Knight(**KNIGHTS["red_knight"])

    result1 = battle(lancelot, mordred)
    result2 = battle(arthur, red_knight)

    print("Battle results:")
    print(f"{lancelot.name} vs {mordred.name}: {result1}")
    print(f"{arthur.name} vs {red_knight.name}: {result2}")


if __name__ == "__main__":
    main()
