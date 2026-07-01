from app.apply_knight_characteristic.apply_armour import apply_armour
from app.apply_knight_characteristic.apply_potion import apply_potion
from app.apply_knight_characteristic.apply_weapon import apply_weapon


def prepare_knight(knights: list[dict]) -> None:
    for knight in knights:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)
