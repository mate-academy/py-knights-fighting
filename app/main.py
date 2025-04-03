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

    def get_hp_after_battle(knight_1: str, knight_2: str) -> int:
        # Get person objects from the 'knights' dictionary by their names
        knight_1_obj = knights[knight_1]
        knight_2_obj = knights[knight_2]

        # Calculating the remaining health points for knight_1 after the battle
        knight_1_hp = (get_hp_of_knight(knight_1_obj)
                       - (get_power_of_knight(knight_2_obj)
                          - get_protection_of_knight(knight_1_obj)
                          )
                       )

        # We restore residual health points
        return max(0, knight_1_hp)  # Return 0, if hp < 0
    # 1 Lancelot vs Mordred:

    lancelot_hp = get_hp_after_battle("lancelot", "mordred")
    mordred_hp = get_hp_after_battle("mordred", "lancelot")

    # 2 Arthur vs Red Knight:
    arthur_hp = get_hp_after_battle("arthur", "red_knight")
    red_knight_hp = get_hp_after_battle("red_knight", "arthur")

    return {
        "Lancelot": lancelot_hp,
        "Arthur": arthur_hp,
        "Mordred": mordred_hp,
        "Red Knight": red_knight_hp,
    }
