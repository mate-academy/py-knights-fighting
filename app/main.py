from app.preparation import get_ready
from app.data_of_knights import KNIGHTS
from app.check_fell import check_fell


def battle(main_dict_knights: dict) -> dict:
    after_preparation = get_ready(main_dict_knights)
    # lancelot stats
    lancelot_hp = after_preparation["lancelot"]["hp"]
    lancelot_power = after_preparation["lancelot"]["power"]
    lancelot_protection = after_preparation["lancelot"]["protection"]

    # arthur stats
    arthur_hp = after_preparation["arthur"]["hp"]
    arthur_power = after_preparation["arthur"]["power"]
    arthur_protection = after_preparation["arthur"]["protection"]

    # mordred stats
    mordred_hp = after_preparation["mordred"]["hp"]
    mordred_power = after_preparation["mordred"]["power"]
    mordred_protection = after_preparation["mordred"]["protection"]

    # red_knight stats
    red_knight_hp = after_preparation["red_knight"]["hp"]
    red_knight_power = after_preparation["red_knight"]["power"]
    red_knight_protection = after_preparation["red_knight"]["protection"]

    # 1 Lancelot vs Mordred:
    lancelot_hp -= mordred_power - lancelot_protection
    mordred_hp -= lancelot_power - mordred_protection

    # check if someone fell in battle
    lancelot_hp = check_fell(lancelot_hp)
    mordred_hp = check_fell(mordred_hp)

    # 2 Arthur vs Red Knight:
    arthur_hp -= red_knight_power - arthur_protection
    red_knight_hp -= arthur_power - red_knight_protection

    # check if someone fell in battle
    arthur_hp = check_fell(arthur_hp)
    red_knight_hp = check_fell(red_knight_hp)

    # Return battle results:
    return {
        after_preparation["lancelot"]["name"]: lancelot_hp,
        after_preparation["arthur"]["name"]: arthur_hp,
        after_preparation["mordred"]["name"]: mordred_hp,
        after_preparation["red_knight"]["name"]: red_knight_hp,
    }


print(battle(KNIGHTS))
