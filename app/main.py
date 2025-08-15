from app.knight.arthur import Arthur
from app.knight.lancelot import Lancelot
from app.knight.mordred import Mordred
from app.knight.redknight import RedKnight
from app.battle.battle import BattleSimulator

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


def battle(knightsconfig: BattleSimulator) -> BattleSimulator:
    # Створення об'єктів лицарів
    lancelot = Lancelot(**knightsconfig["lancelot"])
    arthur = Arthur(**knightsconfig["arthur"])
    mordred = Mordred(**knightsconfig["mordred"])
    red_knight = RedKnight(**knightsconfig["red_knight"])

    # Підготовка лицарів до бою
    lancelot.battle_preparations()
    mordred.battle_preparations()
    arthur.battle_preparations()
    red_knight.battle_preparations()

    # Створення екземпляра симулятора битв
    battle_simulator = BattleSimulator(lancelot, arthur, mordred, red_knight)

    # Запуск битв та отримання результатів
    return battle_simulator.run_all_battles()


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
