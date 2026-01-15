from app.knight_config.config import Knight
from app.battle_preparations.apply_potion_if_exist import Potion
from app.battle_preparations.apply_weapon import Weapon
from app.battle_preparations.apply_armour import Armour
from app.battle.battle_knight_vs_knight import Battle
from app.battle.check import Check


def battle(knights: dict) -> dict:
    knight_list = [
        Knight(knight) for knight in knights.values()
    ]
    for knight in knight_list:
        Potion.potions_effect(knight)
        Weapon.weapon_power(knight)
        knight.protection += Armour.armour_protection(knight.armour)
    for index in range(len(knight_list)):
        if knight_list[index].name == "Lancelot" \
                or knight_list[index].name == "Arthur":
            Check.check_knights(
                Battle.battle(knight_list[index], knight_list[index + 2])
            )
    return Check.result_dict
