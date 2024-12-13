from app.battle_praparation.armour_preparation import armour_preparation
from app.battle_praparation.potion_preparation import potion_preparation
from app.battle_praparation.weapon_preparation import weapon_preparation
from app.knight.one_knight import Knight


def fight_preparation(knight: Knight) -> Knight:
    armour_preparation(knight)
    weapon_preparation(knight)
    potion_preparation(knight)

    return knight
