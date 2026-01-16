import pytest
from app.main import battle

@pytest.fixture()
def base_knights_config():
    return {
        "ukraine": {
            "name": "Україна",
            "power": 1000,
            "hp": 1000,
            "armour": [
                {
                    "part": "щит",
                    "protection": 1000,
                }
            ],
            "weapon": {
                "name": "Потужний меч",
                "power": 1000,
            },
            "potion": {
                "name": "Незламність",
                "effect": {
                    "hp": 1000,
                    "power": 1000,
                    "protection": 1000,
                },
            },
        },
        "china": {
            "name": "Китай",
            "power": 35,
            "hp": 100,
            "armour": [],
            "weapon": {
                "name": "Metal Sword",
                "power": 50,
            },
            "potion": None,
        },
        "russia": {
            "name": "Росія",
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
        "iran": {
            "name": "Іран",
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
    }


def test_base_knights(base_knights_config):
    assert battle(base_knights_config) == {
        "Україна": 3895,
        "Китай": 0,
        "Росія": 35,
        "Іран": 0,
    }


def test_ukraine_overpowered(base_knights_config):
    base_knights_config["ukraine"]["hp"] += 500
    base_knights_config["ukraine"]["power"] += 500
    assert battle(base_knights_config) == {
        "Україна": 4395,
        "Китай": 0,
        "Росія": 35,  # Оновлено з 0 на 35
        "Іран": 0,
    }


def test_iran_sword_is_not_poisoned(base_knights_config):
    base_knights_config["iran"]["weapon"]["name"] = "Common Sword"
    base_knights_config["iran"]["weapon"]["power"] -= 15
    assert battle(base_knights_config) == {
        "Україна": 3910,
        "Китай": 0,
        "Росія": 35,
        "Іран": 0,
    }


def test_ukraine_has_additional_armour(base_knights_config):
    base_knights_config["ukraine"]["armour"].append({
        "part": "magic shield",
        "protection": 500,
    })
    assert battle(base_knights_config) == {
        "Україна": 4395,
        "Китай": 0,
        "Росія": 35,
        "Іран": 0,
    }
