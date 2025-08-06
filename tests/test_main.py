
import pytest
from app.main import create_knight_from_dict
from app.services.battle import battle
from app.models.potion import Potion
from app.models.armour import ArmourPart


@pytest.fixture()
def knights():
    raw_config = {
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
            "armour": [{"part": "breastplate", "protection": 25}],
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

    return {
        name: create_knight_from_dict(cfg)
        for name, cfg in raw_config.items()
    }


def test_base_battle(knights):
    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    assert result1 == {"Lancelot": 0, "Mordred": 35}
    assert result2 == {"Arthur": 30, "Red Knight": 5}


def test_lancelot_overpowered(knights):
    knights["lancelot"].base_hp += 50
    knights["lancelot"].base_power += 50
    knights["lancelot"].apply_equipment()

    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    assert result1 == {"Lancelot": 45, "Mordred": 0}
    assert result2 == {"Arthur": 30, "Red Knight": 5}


def test_red_knight_overpowered(knights):
    knights["red_knight"].base_hp += 50
    knights["red_knight"].base_power += 50
    knights["red_knight"].apply_equipment()

    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    assert result1 == {"Lancelot": 0, "Mordred": 35}
    assert result2 == {"Arthur": 0, "Red Knight": 55}


def test_lancelot_has_armour(knights):
    knights["lancelot"].armour.append(ArmourPart("helmet", 25))
    knights["lancelot"].apply_equipment()

    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    assert result1 == {"Lancelot": 20, "Mordred": 35}
    assert result2 == {"Arthur": 30, "Red Knight": 5}


def test_mordred_sword_is_not_poisoned(knights):
    knights["mordred"].weapon.name = "Common Sword"
    knights["mordred"].weapon.power -= 15
    knights["mordred"].apply_equipment()

    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    assert result1 == {"Lancelot": 10, "Mordred": 35}
    assert result2 == {"Arthur": 30, "Red Knight": 5}


def test_arthur_armour_weak(knights):
    knights["arthur"].armour[0].protection -= 10
    knights["arthur"].armour[1].protection -= 10
    knights["arthur"].armour[2].protection -= 10
    knights["arthur"].apply_equipment()

    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    assert result1 == {"Lancelot": 0, "Mordred": 35}
    assert result2 == {"Arthur": 0, "Red Knight": 5}


def test_arthur_and_lancelot_have_potion(knights):
    knights["arthur"].potion = Potion("Dragon's heart", {
        "protection": 20,
        "power": 10,
        "hp": 10,
    })
    knights["lancelot"].potion = Potion("Magic Power", {
        "power": 25,
        "hp": 10,
    })
    knights["arthur"].apply_equipment()
    knights["lancelot"].apply_equipment()

    result1 = battle(knights["lancelot"], knights["mordred"])
    result2 = battle(knights["arthur"], knights["red_knight"])

    assert result1 == {"Lancelot": 5, "Mordred": 10}
    assert result2 == {"Arthur": 60, "Red Knight": 0}
