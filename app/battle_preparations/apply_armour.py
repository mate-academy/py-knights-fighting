from app.battle_preparations.load_from_file import to_create_knight
from app.battle_preparations.knights import ready_knights


def apply_armour(knights_dict: dict) -> list:
    knights = to_create_knight(knights_dict)
    armoured_knights = ready_knights(knights_dict)

    for index, knight in enumerate(knights):
        if knight["armour"]:
            for item in knight["armour"]:
                armoured_knights[index].protection = (
                    armoured_knights[index].protection
                    + item["protection"])

    return armoured_knights
