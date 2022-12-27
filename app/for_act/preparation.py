from app.for_knight.armour import apply_armour
from app.for_knight.potion import apply_potion
from app.for_knight.weapon import apply_weapon
from typing import Callable


def prepare_to_the_battle(fighter: dict) -> Callable:
    apply_armour(fighter)
    apply_weapon(fighter)
    apply_potion(fighter)
