from app.battle.knight import Knight


def battle(config: dict) -> dict:
    # Create Knight instances
    knights = {}
    for knight_name, knight_attributes in config.items():
        knights[knight_name] = Knight(
            name=knight_attributes["name"],
            power=knight_attributes["power"],
            hp=knight_attributes["hp"],
            armour=knight_attributes.get("armour", []),
            weapon=knight_attributes["weapon"],
            potion=knight_attributes.get("potion", None)
        )

    # Lancelot vs Mordred, Arthur vs Red Knight
    battle_results = {}

    battle_results.update(Knight.battle(
        knights["lancelot"],
        knights["mordred"]
    ))

    battle_results.update(Knight.battle(
        knights["arthur"],
        knights["red_knight"]
    ))

    # Instead of printing, return the battle results
    return battle_results
