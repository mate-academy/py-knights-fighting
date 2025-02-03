import pytest

from app.main import battle


@pytest.fixture()
def base_knights_config():
    return {
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
                }
            ],
            "weapon": {"name": "Sword", "power": 45},
            "potion": {
                "name": "Blessing",
                "effect": {
                    "hp": +10,
                    "power": +5,
                },
            },
        },
    }


def test_base_knights(base_knights_config):
    assert battle(base_knights_config) == {
        "Lancelot": 0,
        "Arthur": 30,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_lancelot_overpowered(base_knights_config):
    base_knights_config["lancelot"]["hp"] += 50
    base_knights_config["lancelot"]["power"] += 50
    assert battle(base_knights_config) == {
        "Lancelot": 45,
        "Arthur": 30,
        "Mordred": 0,
        "Red Knight": 5,
    }


def test_red_knight_overpowered(base_knights_config):
    base_knights_config["red_knight"]["hp"] += 50
    base_knights_config["red_knight"]["power"] += 50
    assert battle(base_knights_config) == {
        "Lancelot": 0,
        "Arthur": 0,
        "Mordred": 35,
        "Red Knight": 55,
    }


def test_lancelot_has_armour(base_knights_config):
    base_knights_config["lancelot"]["armour"].append({
        "part": "helmet",
        "protection": 25,
    })
    assert battle(base_knights_config) == {
        "Lancelot": 20,
        "Arthur": 30,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_mordred_sword_is_not_poisoned(base_knights_config):
    base_knights_config["mordred"]["weapon"]["name"] = "Common Sword"
    base_knights_config["mordred"]["weapon"]["power"] -= 15
    assert battle(base_knights_config) == {
        "Lancelot": 10,
        "Arthur": 30,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_arthur_armour_weak(base_knights_config):
    base_knights_config["arthur"]["armour"][0]["protection"] -= 10
    base_knights_config["arthur"]["armour"][1]["protection"] -= 10
    base_knights_config["arthur"]["armour"][0]["protection"] -= 10
    assert battle(base_knights_config) == {
        "Lancelot": 0,
        "Arthur": 0,
        "Mordred": 35,
        "Red Knight": 5,
    }


def test_arthur_and_lancelot_have_potion(base_knights_config):
    base_knights_config["arthur"]["potion"] = {
        "name": "Dragon's heart",
        "effect": {
            "protection": +20,
            "power": +10,
            "hp": +10,
        }
    }
    base_knights_config["lancelot"]["potion"] = {
        "name": "Magic Power",
        "effect": {
            "power": +25,
            "hp": +10,
        }
    }
    assert battle(base_knights_config) == {
        "Lancelot": 5,
        "Arthur": 60,
        "Mordred": 10,
        "Red Knight": 0,
    }

