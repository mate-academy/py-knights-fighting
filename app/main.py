from typing import Dict, Any, List, Tuple

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
    # Подготовка всех рыцарей (генератор словарей)
    prepared = {
        name: prepare_knight(data) for name,
        data in knights_config.items()
    }

    # Определение пар для боёв (можно легко добавить новые)
    battles: List[Tuple[str, str]] = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    # Проведение боёв
    for knight1_key, knight2_key in battles:
        k1 = prepared[knight1_key]
        k2 = prepared[knight2_key]

        # Обоюдная атака
        k1["hp"] -= k2["power"] - k1["protection"]
        k2["hp"] -= k1["power"] - k2["protection"]

        # Здоровье не может быть отрицательным
        k1["hp"] = max(k1["hp"], 0)
        k2["hp"] = max(k2["hp"], 0)

    # Формирование результата (используем поле "name" из данных рыцаря)
    return {prepared[name]["name"]: prepared[name]["hp"] for name in prepared}


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
                "power": 15,
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
