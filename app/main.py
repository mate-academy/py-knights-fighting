from app.battle.fight import battle_fight
from app.battle_preparation.apply_armour import apply_armour
from app.battle_preparation.apply_potion import apply_potion
from app.battle_preparation.apply_weapon import apply_weapon


def battle(base_knights_config):
    for knight in base_knights_config.values():
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    return battle_fight(base_knights_config)
