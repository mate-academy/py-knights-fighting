from app.Battle_Preparations.apply_weapon import apply_weapon
from app.Battle_Preparations.apply_armour import apply_armour
from app.Battle_Preparations.apply_potion import apply_potion


def battle(knights: dict) -> dict:
    # apply weapon
    apply_weapon(knights)
    # apply armour
    apply_armour(knights)
    # apply potion
    apply_potion(knights)
    result = {}
    knights_list = list(knights.values())
    for stats in range(0, len(knights_list) // 2):
        first_knight = knights_list[stats]
        second_knight = knights_list[stats + 2]
        first_knight["hp"] -= (second_knight["power"]
                               - first_knight["protection"])
        second_knight["hp"] -= (first_knight["power"]
                                - second_knight["protection"])
        if first_knight["hp"] <= 0:
            first_knight["hp"] = 0
        if second_knight["hp"] <= 0:
            second_knight["hp"] = 0
        result.update({
            first_knight["name"]: first_knight["hp"],
            second_knight["name"]: second_knight["hp"]
        })
    return result
