from app.Knights.Arthur.arthur import Arthur
from app.Knights.Red_Knight.red_knight import RedKnight
from app.Knights.Lancelot.lancelot import Lancelot
from app.Knights.Mordred.mordred import Mordred

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "attack": 10,
        "defense": 8,
        "hp": 100,
        "power": 15,
        "armour": [{"protection": 5}],
        "weapon": {"name": "Sword", "power": 5},
        "potion": {"effect": {"hp": 10, "power": 2}},
    },
    "arthur": {
        "name": "Arthur",
        "attack": 12,
        "defense": 9,
        "hp": 100,
        "power": 18,
        "armour": [{"protection": 6}],
        "weapon": {"name": "Excalibur", "power": 10},
        "potion": {"effect": {"protection": 3}},
    },
    "mordred": {
        "name": "Mordred",
        "attack": 11,
        "defense": 7,
        "hp": 100,
        "power": 14,
        "armour": [{"protection": 4}],
        "weapon": {"name": "Dark Blade", "power": 7},
        "potion": {"effect": {"power": 5}},
    },
    "red_knight": {
        "name": "Red Knight",
        "attack": 9,
        "defense": 10,
        "hp": 100,
        "power": 16,
        "armour": [{"protection": 7}],
        "weapon": {"name": "Battle Axe", "power": 8},
        "potion": {"effect": {"hp": 15}},
    },
}


def battle(knights_config: dict) -> dict:
    lancelot = Lancelot(knights_config)
    arthur = Arthur(knights_config)
    mordred = Mordred(knights_config)
    red_knight = RedKnight(knights_config)

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
