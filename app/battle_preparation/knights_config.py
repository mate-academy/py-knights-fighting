from app.battle_preparation.armour import apply_armour
from app.battle_preparation.weapon import apply_weapon
from app.battle_preparation.potion import apply_potion


def knight_config(knight_config: dict) -> None:
    apply_armour(knight_config)
    apply_weapon(knight_config)
    apply_potion(knight_config)
