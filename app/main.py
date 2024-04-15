from app.knight import Knight


def battle(knightsconfig: dict) -> dict:
    # Create instances of Knight class for each knight
    lancelot = Knight(**knightsconfig["lancelot"])
    arthur = Knight(**knightsconfig["arthur"])
    mordred = Knight(**knightsconfig["mordred"])
    red_knight = Knight(**knightsconfig["red_knight"])

    # Apply armour, weapon, and potion effects for each knight
    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    # BATTLE:
    lancelot_hp = max(0, lancelot.hp - (mordred.power - lancelot.protection))
    mordred_hp = max(0, mordred.hp - (lancelot.power - mordred.protection))
    arthur_hp = max(0, arthur.hp - (red_knight.power - arthur.protection))
    red_knight_hp = max(0, red_knight.hp - (arthur.power
                                            - red_knight.protection))

    return {
        lancelot.name: lancelot_hp,
        arthur.name: arthur_hp,
        mordred.name: mordred_hp,
        red_knight.name: red_knight_hp,
    }


def main() -> None:
    # Define knights configuration
    knightsconfig = {
        "lancelot": {
            "name": "Lancelot",
            "hp": 100,
            "power": 30,
            "armour": [],
            "weapon": {"name": "Excalibur", "power": 20},
            "potion": None,
        },
        "arthur": {
            "name": "Arthur",
            "hp": 70,
            "power": 25,
            "armour": [{"part": "helmet", "protection": 15},
                       {"part": "breastplate", "protection": 20}],
            "weapon": {"name": "Excalibur", "power": 20},
            "potion": {"name": "Dragon's heart",
                       "effect": {"protection": 20, "power": 10, "hp": 10}},
        },
        "mordred": {
            "name": "Mordred",
            "hp": 80,
            "power": 25,
            "armour": [],
            "weapon": {"name": "Poisoned Sword", "power": 30},
            "potion": None,
        },
        "red_knight": {
            "name": "Red Knight",
            "hp": 120,
            "power": 20,
            "armour": [{"part": "helmet", "protection": 15},
                       {"part": "breastplate", "protection": 25}],
            "weapon": {"name": "Axe", "power": 25},
            "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
        },
    }

    # Start the battle
    result = battle(knightsconfig)

    # Print the result
    print("Battle Result:")
    for knight, hp in result.items():
        print(f"{knight}: {hp} HP")
