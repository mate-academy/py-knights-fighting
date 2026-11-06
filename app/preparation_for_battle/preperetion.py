from app.character.knight import Knight
from app.inventory.equipment import Equipment


def preparation_for_battle(knights: dict) -> list:
    list_of_knights = []
    for knight in knights.values():
        fighter = Knight(
            knight["name"],
            knight["power"],
            knight["hp"]
        )
        fighter_equipment = Equipment(
            knight["armour"],
            knight["weapon"],
            knight["potion"]
        )
        fighter_equipment.knight_buff(fighter)
        list_of_knights.append(fighter)

    return list_of_knights
