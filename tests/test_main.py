import pytest
from typing import Dict, Any

from app.battle.logic import fight
from app.knights.knight import Knight


@pytest.fixture()
def base_knights_config() -> Dict[str, Dict[str, Any]]:
    return {
        "lancelot": {
            "name": "Lancelot",
            "power": 35,
            "hp": 100,
            "armour": [],
            "weapon": {"name": "Metal Sword", "power": 50},
            "potion": None,
        },
        "arthur": {
            "name": "Arthur",
            "power": 45,
            "hp": 75,
            "armour": [
                {"part": "helmet", "protection": 15},
                {"part": "breastplate", "protection": 20},
                {"part": "boots", "protection": 10},
            ],
            "weapon": {"name": "Two-handed Sword", "power": 55},
            "potion": None,
        },
        "mordred": {
            "name": "Mordred",
            "power": 30,
            "hp": 90,
            "armour": [
                {"part": "breastplate", "protection": 15},
                {"part": "boots", "protection": 10},
            ],
            "weapon": {"name": "Poisoned Sword", "power": 60},
            "potion": {
                "name": "Berserk",
                "effect": {"power": +15, "hp": -5, "protection": +10},
            },
        },
        "red_knight": {
            "name": "Red Knight",
            "power": 40,
            "hp": 70,
            "armour": [{"part": "breastplate", "protection": 25}],
            "weapon": {"name": "Sword", "power": 45},
            "potion": {"name": "Blessing", "effect": {"hp": +10, "power": +5}},
        },
    }


def run_battle(cfg: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    names = ["lancelot", "arthur", "mordred", "red_knight"]
    knights = {name: Knight(cfg[name]) for name in names}

    res1 = fight(knights["lancelot"], knights["mordred"])
    res2 = fight(knights["arthur"], knights["red_knight"])

    return {
        knights["lancelot"].name: res1[knights["lancelot"].name],
        knights["mordred"].name: res1[knights["mordred"].name],
        knights["arthur"].name: res2[knights["arthur"].name],
        knights["red_knight"].name: res2[knights["red_knight"].name],
    }

def test_base_knights(base_knights_config: Dict[str, Dict[str, Any]]) -> None:
    assert run_battle(base_knights_config) == {
        "Lancelot": 0,
        "Arthur": 30,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_lancelot_overpowered(base_knights_config: Dict[str, Dict[str, Any]]) -> None:
    base_knights_config["lancelot"]["hp"] += 50
    base_knights_config["lancelot"]["power"] += 50
    assert run_battle(base_knights_config) == {
        "Lancelot": 45,
        "Arthur": 30,
        "Mordred": 0,
        "Red Knight": 5,
    }


def test_red_knight_overpowered(base_knights_config: Dict[str, Dict[str, Any]]) -> None:
    base_knights_config["red_knight"]["hp"] += 50
    base_knights_config["red_knight"]["power"] += 50
    assert run_battle(base_knights_config) == {
        "Lancelot": 0,
        "Arthur": 0,
        "Mordred": 35,
        "Red Knight": 55,
    }


def test_lancelot_has_armour(base_knights_config: Dict[str, Dict[str, Any]]) -> None:
    base_knights_config["lancelot"]["armour"].append(
        {"part": "helmet", "protection": 25}
    )
    assert run_battle(base_knights_config) == {
        "Lancelot": 20,
        "Arthur": 30,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_mordred_sword_is_not_poisoned(base_knights_config: Dict[str, Dict[str, Any]]) -> None:
    base_knights_config["mordred"]["weapon"]["name"] = "Common Sword"
    base_knights_config["mordred"]["weapon"]["power"] -= 15
    assert run_battle(base_knights_config) == {
        "Lancelot": 10,
        "Arthur": 30,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_arthur_armour_weak(base_knights_config: Dict[str, Dict[str, Any]]) -> None:
    base_knights_config["arthur"]["armour"][0]["protection"] -= 10
    base_knights_config["arthur"]["armour"][1]["protection"] -= 10
    base_knights_config["arthur"]["armour"][2]["protection"] -= 10
    assert run_battle(base_knights_config) == {
        "Lancelot": 0,
        "Arthur": 0,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_arthur_and_lancelot_have_potion(base_knights_config: Dict[str, Dict[str, Any]]) -> None:
    base_knights_config["arthur"]["potion"] = {
        "name": "Dragon's heart",
        "effect": {"protection": +20, "power": +10, "hp": +10},
    }
    base_knights_config["lancelot"]["potion"] = {
        "name": "Magic Power",
        "effect": {"power": +25, "hp": +10},
    }
    assert run_battle(base_knights_config) == {
        "Lancelot": 5,
        "Arthur": 60,
        "Mordred": 10,
        "Red Knight": 0,
    }
