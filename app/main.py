from typing import Dict, Any


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
            },
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
            },
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
            },
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            },
        ],
        "weapon": {
            "name": "Sword",
            "power": 45,
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def _apply_armour(knight: Dict[str, Any]) -> None:
    """Суммируем защиту всей брони и записываем в knight['protection']."""
    knight["protection"] = 0
    for armour_piece in knight["armour"]:
        knight["protection"] += armour_piece["protection"]


def _apply_weapon(knight: Dict[str, Any]) -> None:
    """Добавляем силу оружия к общей силе рыцаря."""
    knight["power"] += knight["weapon"]["power"]


def _apply_potion(knight: Dict[str, Any]) -> None:
    """Если есть зелье, добавляем эффекты (power, protection, hp)."""
    potion = knight["potion"]
    if potion is None:
        return

    effect = potion["effect"]

    if "power" in effect:
        knight["power"] += effect["power"]

    if "protection" in effect:
        knight["protection"] += effect["protection"]

    if "hp" in effect:
        knight["hp"] += effect["hp"]


def _prepare_knight(knight: Dict[str, Any]) -> None:
    """Полная подготовка рыцаря перед боем."""
    _apply_armour(knight)
    _apply_weapon(knight)
    _apply_potion(knight)


def _duel(
    first_knight: Dict[str, Any],
    second_knight: Dict[str, Any],
) -> None:
    """
    Обмен ударами между двумя рыцарями.
    ХП не уходит ниже нуля (как в исходной логике).
    """
    first_knight["hp"] -= (
        second_knight["power"] - first_knight["protection"]
    )
    second_knight["hp"] -= (
        first_knight["power"] - second_knight["protection"]
    )

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0
    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """
    Готовим всех рыцарей, проводим два поединка и
    возвращаем итоговые HP по именам.
    """

    # подготовка
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    for knight_data in (lancelot, arthur, mordred, red_knight):
        _prepare_knight(knight_data)

    # бой: Lancelot vs Mordred
    _duel(lancelot, mordred)

    # бой: Arthur vs Red Knight
    _duel(arthur, red_knight)

    # результат
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
