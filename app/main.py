from typing import Dict, Any

# Описания типов для удобства
KnightData = Dict[str, Any]
BattleResult = Dict[str, int]


def prepare_knight(knight: KnightData) -> KnightData:
    """
    Принимает исходные данные рыцаря, возвращает словарь с вычисленными
    параметрами после применения брони, оружия и зелья.
    """
    # Создаём копию, чтобы не изменять оригинал
    prepared = knight.copy()
    prepared["protection"] = 0

    # Броня
    for armour in prepared["armour"]:
        prepared["protection"] += armour["protection"]

    # Оружие
    prepared["power"] += prepared["weapon"]["power"]

    # Зелье
    potion = prepared.get("potion")
    if potion is not None:
        effect = potion["effect"]
        if "power" in effect:
            prepared["power"] += effect["power"]
        if "protection" in effect:
            prepared["protection"] += effect["protection"]
        if "hp" in effect:
            prepared["hp"] += effect["hp"]

    return prepared


def battle(knights_config: Dict[str, KnightData]) -> BattleResult:
    """
    Проводит турнир между рыцарями согласно заданной конфигурации.
    Возвращает словарь с итоговым здоровьем каждого рыцаря.
    """
    # Подготовка рыцарей (работаем с копиями)
    lancelot = prepare_knight(knights_config["lancelot"])
    arthur = prepare_knight(knights_config["arthur"])
    mordred = prepare_knight(knights_config["mordred"])
    red_knight = prepare_knight(knights_config["red_knight"])

    # 1-й бой: Lancelot vs Mordred
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # Проверка на выживание
    lancelot["hp"] = max(lancelot["hp"], 0)
    mordred["hp"] = max(mordred["hp"], 0)

    # 2-й бой: Arthur vs Red Knight
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    arthur["hp"] = max(arthur["hp"], 0)
    red_knight["hp"] = max(red_knight["hp"], 0)

    # Формирование результата
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


# Конфигурация рыцарей остаётся без изменений
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
                "power": 15,        # убрали устаревший +
                "hp": -5,
                "protection": 10,
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
                "hp": 10,
                "power": 5,
            }
        }
    }
}


if __name__ == "__main__":
    print(battle(KNIGHTS))
