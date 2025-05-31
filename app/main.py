from __future__ import annotations
from typing import Dict
from app.config.knights import KNIGHTS
from app.models.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    damage1 = max(0, knight2.power - knight1.protection)
    damage2 = max(0, knight1.power - knight2.protection)
    knight1.hp = max(0, knight1.hp - damage1)
    knight2.hp = max(0, knight2.hp - damage2)


def battle(knights_config: Dict) -> Dict[str, int]:
    knights = {
        name: Knight(**data)
        for name, data in knights_config.items()
    }

    # Проводим битвы по условию задачи
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


if __name__ == "__main__":
    print("Результаты битвы:", battle(KNIGHTS))