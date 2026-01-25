from app.battle_preparations.utils import (apply_weapon,
                                           apply_potion,
                                           apply_armour)


def count_hp(knight: dict, opponent: dict) -> dict:
    knight["hp"] -= (opponent["power"] - knight["protection"])
    if knight["hp"] <= 0:
        knight["hp"] = 0
    return {knight["name"]: knight["hp"]}


def battle(knights: dict) -> dict:
    apply_weapon(knights)
    apply_armour(knights)
    apply_potion(knights)
    result = {}
    knights_list = list(knights.values())
    for stats in range(0, len(knights_list) // 2):
        first_knight = knights_list[stats]
        second_knight = knights_list[stats + 2]
        result.update(count_hp(first_knight, second_knight))
        result.update(count_hp(second_knight, first_knight))

    return result
