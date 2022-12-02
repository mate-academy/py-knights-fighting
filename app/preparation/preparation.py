from __future__ import annotations
from app.class_knight.knight import Knight


def preparation(knights_config: dict) -> Knight:
    for key, value in knights_config.items():
        current_knight = Knight(value["name"], value["power"], value["hp"])
        current_knight.protection = 0
        if len(value["armour"]) > 0:
            for armour in value["armour"]:
                current_knight.protection += armour["protection"]
        current_knight.power += value["weapon"]["power"]
        if value["potion"] is not None:
            current_knight.power += value["potion"]["effect"]["power"]
            current_knight.hp += value["potion"]["effect"]["hp"]
            if value["potion"]["effect"].get("protection") is not None:
                current_knight.protection += \
                    value["potion"]["effect"]["protection"]
    return Knight.knights
