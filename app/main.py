from copy import deepcopy
from app.knights.models import Knight


KNIGHT_ORDER = ["lancelot", "mordred", "arthur", "red_knight"]


def _create_knight(conf: dict) -> Knight:
    return Knight(
        conf["name"],
        conf["hp"],
        conf["power"],
        conf.get("armour"),
        conf.get("weapon"),
        conf.get("potion"),
    )


def _fight(first: dict, second: dict) -> tuple[int, int]:
    damage_to_first = max(0, second["power"] - first["protection"])
    damage_to_second = max(0, first["power"] - second["protection"])

    new_first_hp = max(0, first["hp"] - damage_to_first)
    new_second_hp = max(0, second["hp"] - damage_to_second)

    return new_first_hp, new_second_hp


def battle(knights_config: dict) -> dict:
    knights = deepcopy(knights_config)

    created_knights = {
        name: _create_knight(knights[name])
        for name in KNIGHT_ORDER
    }

    stats = {
        name: knight.prepare_stats()
        for name, knight in created_knights.items()
    }

    l_hp, m_hp = _fight(stats["lancelot"], stats["mordred"])
    a_hp, r_hp = _fight(stats["arthur"], stats["red_knight"])

    return {
        created_knights["lancelot"].name: l_hp,
        created_knights["arthur"].name: a_hp,
        created_knights["mordred"].name: m_hp,
        created_knights["red_knight"].name: r_hp,
    }
