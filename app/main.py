from __future__ import annotations

from typing import Dict, Any

from app.entities import ArmorPiece, Weapon, Potion, Knight
from app.arena import duel_stats
from app.config import KNIGHTS


def _build_knight(raw_knight: Dict[str, Any]) -> Knight:
    """
    Превращаем словарь из KNIGHTS в объект Knight:
    - armour -> список ArmorPiece
    - weapon -> Weapon | None
    - potion -> Potion | None
    """
    armour_pieces = [
        ArmorPiece(
            part=piece["part"],
            protection=piece["protection"],
        )
        for piece in raw_knight["armour"]
    ]

    # оружие (может отсутствовать)
    weapon_raw = raw_knight.get("weapon")
    if weapon_raw is not None:
        weapon_obj = Weapon(
            name=weapon_raw["name"],
            power=weapon_raw["power"],
        )
    else:
        weapon_obj = None

    # зелье (может отсутствовать)
    potion_raw = raw_knight.get("potion")
    if potion_raw is not None:
        potion_obj = Potion(
            name=potion_raw["name"],
            effect=potion_raw["effect"],
        )
    else:
        potion_obj = None

    return Knight(
        name=raw_knight["name"],
        base_hp=raw_knight["hp"],
        base_power=raw_knight["power"],
        armour=armour_pieces,
        weapon=weapon_obj,
        potion=potion_obj,
    )


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """
    Совместимая с тестами функция:
    принимает словарь рыцарей в исходном формате (как KNIGHTS),
    моделирует два поединка:
      - Lancelot vs Mordred
      - Arthur vs Red Knight
    и возвращает итоговые HP всех четырёх рыцарей.
    """
    # строим объекты Knight
    lancelot_obj = _build_knight(knights_config["lancelot"])
    arthur_obj = _build_knight(knights_config["arthur"])
    mordred_obj = _build_knight(knights_config["mordred"])
    red_knight_obj = _build_knight(knights_config["red_knight"])

    # дуэль 1: Lancelot vs Mordred
    duel_one_result = duel_stats(lancelot_obj, mordred_obj)
    # дуэль 2: Arthur vs Red Knight
    duel_two_result = duel_stats(arthur_obj, red_knight_obj)

    # объединяем результаты двух поединков в один словарь
    final_result: Dict[str, int] = {}
    final_result.update(duel_one_result)
    final_result.update(duel_two_result)

    return final_result


def main() -> Dict[str, int]:
    """Точка входа при ручном запуске."""
    return battle(KNIGHTS)


if __name__ == "__main__":
    print(main())
