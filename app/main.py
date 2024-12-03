from app.battle.battlefront import battle

base_knights_config = {
    "lancelot": {
        "name": "Lancelot",
        "power": 60,
        "hp": 100,
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "shield", "protection": 20},
        ],
        "weapon": {"name": "Excalibur", "power": 15},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 50,
        "hp": 120,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
        ],
        "weapon": {"name": "Holy Sword", "power": 10},
        "potion": {"name": "Healing Potion", "effect": {"hp": 20}},
    },
    "mordred": {
        "name": "Mordred",
        "power": 70,
        "hp": 90,
        "armour": [{"part": "shield", "protection": 25}],
        "weapon": {"name": "Poisoned Dagger", "power": 20},
        "potion": None,
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {"part": "helmet", "protection": 10},
            {"part": "breastplate", "protection": 15},
        ],
        "weapon": {"name": "Spear", "power": 10},
        "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
    },
}

if __name__ == "__main__":

    battle_results = battle(base_knights_config)

    print("Battle Results:")
    for knight, hp in battle_results.items():
        print(f"{knight}: {hp}")
