from app.functions_for_battle.apply_armour import apply_armour
from app.functions_for_battle.apply_potion import apply_potion


def get_ready_to_battle(knight: dict) -> None:
    apply_armour(knight)

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    apply_potion(knight)
