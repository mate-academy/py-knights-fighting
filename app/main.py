from app.knights.knight import Knight
from app.knights.equipment import Armor, Weapon, Potion
from app.battle.fight import fight


def create_knights(config: dict) -> dict:
    knights = {}
    for knight_name, attributes in config.items():
        armor = [Armor(
            a["part"], a["protection"]
        ) for a in attributes["armour"]]
        weapon = Weapon(
            attributes["weapon"]["name"],
            attributes["weapon"]["power"]
        )
        potion = Potion(
            attributes["potion"]["name"],
            attributes["potion"]["effect"]
        ) if attributes["potion"] else None
        knights[knight_name] = Knight(
            attributes["name"],
            attributes["power"],
            attributes["hp"],
            armor,
            weapon,
            potion
        )
    return knights


def battle(knights_config: dict) -> dict:
    knights = create_knights(knights_config)
    # Execute Lancelot vs Mordred and Arthur vs Red Knight
    result1 = fight(knights["lancelot"], knights["mordred"])
    result2 = fight(knights["arthur"], knights["red_knight"])

    # Combine results
    return {**result1, **result2}


if __name__ == "__main__":
    KNIGHTS = {
        "lancelot": {...},  # Insert knight configurations
        "arthur": {...},
        "mordred": {...},
        "red_knight": {...}
    }
    print(battle(KNIGHTS))
