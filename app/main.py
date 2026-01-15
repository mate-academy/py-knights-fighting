from __future__ import annotations

from typing import Dict, Any

from app.arena import duel_stats, build_knight
from app.config import KNIGHTS
from app.entities import Knight  # используется в type hints


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """
    Принимает словарь рыцарей (как KNIGHTS),
    симулирует два поединка:
      1) Lancelot vs Mordred
      2) Arthur vs Red Knight
    Возвращает словарь {имя_рыцаря: итоговое_хп}.
    """

    # Собираем всех рыцарей через dict comprehension,
    # чтобы не дублировать код 4 раза.
    knights_objs: Dict[str, Knight] = {
        name: build_knight(raw_knight)
        for name, raw_knight in knights_config.items()
    }

    # Дуэль №1: Lancelot vs Mordred
    duel_one_result = duel_stats(
        knights_objs["lancelot"],
        knights_objs["mordred"],
    )

    # Дуэль №2: Arthur vs Red Knight
    duel_two_result = duel_stats(
        knights_objs["arthur"],
        knights_objs["red_knight"],
    )

    # Склеиваем результаты двух дуэлей
    final_result: Dict[str, int] = {}
    final_result.update(duel_one_result)
    final_result.update(duel_two_result)

    return final_result


def main() -> Dict[str, int]:
    """Точка входа для ручного запуска (не используется тестами напрямую)."""
    return battle(KNIGHTS)


if __name__ == "__main__":
    print(main())
