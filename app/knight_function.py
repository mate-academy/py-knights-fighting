from typing import Dict, Union


def prepare_knight(
        knight: Dict[
            str, Union[
                str, int, list, Dict[
                    str, Union[
                        str, int, list, Dict[str, int]
                    ]
                ]
            ]
        ]
) -> Dict[str, Union[str, int]]:

    protection = 0
    for a_armour in knight["armour"]:
        protection += a_armour["protection"]

    power = knight["power"] + knight["weapon"]["power"]

    potion = knight["potion"]
    if potion:
        effects = potion.get("effect", {})
        power += effects.get("power", 0)
        protection += effects.get("protection", 0)
        hp = knight["hp"] + effects.get("hp", 0)
    else:
        hp = knight["hp"]

    return {
        "name": knight["name"],
        "power": power,
        "protection": protection,
        "hp": hp,
    }


def battle(knights: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    prepared_knights = {
        name: prepare_knight(knight)
        for name, knight in knights.items()
    }

    lancelot = prepared_knights["lancelot"]
    mordred = prepared_knights["mordred"]
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur = prepared_knights["arthur"]
    red_knight = prepared_knights["red_knight"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for name in prepared_knights:
        knight = prepared_knights[name]
        if knight["hp"] < 0:
            knight["hp"] = 0

    return {
        name.replace("_", " ").title(): knight["hp"]
        for name,
        knight in prepared_knights.items()
    }
