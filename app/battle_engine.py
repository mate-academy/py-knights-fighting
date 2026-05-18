from typing import Any


def _get_armour_protection(knight: dict[str, Any]) -> int:
    return sum(part["protection"] for part in knight["armour"])


def _prepare_knight(knight: dict[str, Any]) -> dict[str, int | str]:
    prepared_knight = {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"] + knight["weapon"]["power"],
        "protection": _get_armour_protection(knight),
    }
    potion = knight["potion"]

    if potion is None:
        return prepared_knight

    for stat, modifier in potion["effect"].items():
        prepared_knight[stat] += modifier

    return prepared_knight


def _run_duel(first_knight: dict[str, int | str],
              second_knight: dict[str, int | str]) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0


def battle(knights_config: dict[str, dict[str, Any]]) -> dict[str, int]:
    lancelot = _prepare_knight(knights_config["lancelot"])
    arthur = _prepare_knight(knights_config["arthur"])
    mordred = _prepare_knight(knights_config["mordred"])
    red_knight = _prepare_knight(knights_config["red_knight"])

    _run_duel(lancelot, mordred)
    _run_duel(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
