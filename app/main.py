from app.battle import Battle


def battle(knightconfig: dict) -> dict:
    battle_instance = Battle(knightconfig)
    battle_instance.apply_knight_modifiers()
    results = battle_instance.fight()
    return results
