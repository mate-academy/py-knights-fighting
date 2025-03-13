from app.battle.battle import battle

# Исходные данные
KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [{"part": "helmet", "protection": 15}],
        "weapon": {"name": "Sword", "power": 50},
        "potion": {"name": "Strength", "effect": {"power": 10}},
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [{"part": "breastplate", "protection": 20}],
        "weapon": {"name": "Excalibur", "power": 60},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [{"part": "boots", "protection": 10}],
        "weapon": {"name": "Axe", "power": 55},
        "potion": {"name": "Poison", "effect": {"hp": -20}},
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


def main() -> None:
    """Основная функция для запуска битвы."""
    result = battle(KNIGHTS)
    print(result)


if __name__ == "__main__":
    main()
