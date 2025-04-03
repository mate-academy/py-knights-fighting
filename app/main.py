from app.knight.knight import Knight
from app.knight.knight import get_hp_of_knight
from app.knight.knight import get_power_of_knight
from app.knight.knight import get_protection_of_knight


def battle(knights_dict: dict) -> dict:
    knights = {
        "lancelot": Knight(
            knights_dict["lancelot"], knights_dict["lancelot"]["potion"]
        ),
        "arthur": Knight(
            knights_dict["arthur"], knights_dict["arthur"]["potion"]
        ),
        "mordred": Knight(
            knights_dict["mordred"], knights_dict["mordred"]["potion"]
        ),
        "red_knight": Knight(
            knights_dict["red_knight"], knights_dict["red_knight"]["potion"]
        ),
    }

    # 1 Lancelot vs Mordred:
    lancelot_hp = get_hp_of_knight(knights["lancelot"])
    lancelot_hp -= (get_power_of_knight(knights["mordred"])
                    - get_protection_of_knight(knights["lancelot"]))
    mordred_hp = get_hp_of_knight(knights["mordred"])
    mordred_hp -= (get_power_of_knight(knights["lancelot"])
                   - get_protection_of_knight(knights["mordred"]))

    if lancelot_hp <= 0:
        lancelot_hp = 0
    if mordred_hp <= 0:
        mordred_hp = 0

    # 2 Arthur vs Red Knight:
    arthur_hp = get_hp_of_knight(knights["arthur"])
    arthur_hp -= (get_power_of_knight(knights["red_knight"])
                  - get_protection_of_knight(knights["arthur"]))
    red_knight_hp = get_hp_of_knight(knights["red_knight"])
    red_knight_hp -= (get_power_of_knight(knights["arthur"])
                      - get_protection_of_knight(knights["red_knight"]))

    if arthur_hp <= 0:
        arthur_hp = 0
    if red_knight_hp <= 0:
        red_knight_hp = 0

    return {
        "Lancelot": lancelot_hp,
        "Arthur": arthur_hp,
        "Mordred": mordred_hp,
        "Red Knight": red_knight_hp,
    }
