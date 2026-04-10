from app.knight import Knight
from app.battle_calc import battle_calc


def battle(knights_config: dict) -> dict:
    # creating knight instances
    knight_obj_dict = {}
    for knight in knights_config.values():
        knight_obj = Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=knight["armour"],
            weapon=knight["weapon"],
            potion=knight["potion"]
        )
        knight_obj_dict[knight["name"]] = knight_obj

    # battle preparations
    for knight in knight_obj_dict.values():
        knight.protection_calc()
        knight.power_calc()
        knight.potion_calc()

    # BATTLE
    # Lancelot vs Mordred
    first_battle_res = battle_calc(
        knight_obj_dict["Lancelot"],
        knight_obj_dict["Mordred"]
    )
    # Arthur vs Red Knight
    second_battle_res = battle_calc(
        knight_obj_dict["Arthur"],
        knight_obj_dict["Red Knight"]
    )

    # results
    return {
        "Lancelot": first_battle_res[0],
        "Mordred": first_battle_res[1],
        "Arthur": second_battle_res[0],
        "Red Knight": second_battle_res[1],
    }
