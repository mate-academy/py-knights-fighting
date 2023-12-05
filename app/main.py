from app.battle_preparation.initial_data import knights
from app.battle_preparation.battle import final_battle
from app.knights.knight import Knight


def battle(knights_in_dictionary: dict) -> dict:
    ready_knights = []
    for knight in knights_in_dictionary:
        create_knight = Knight(
            knights_in_dictionary[knight]["name"],
            knights_in_dictionary[knight]["power"],
            knights_in_dictionary[knight]["hp"]
        )
        ready_knights.append(
            Knight.apply_equipment(
                Knight.update_knight(
                    create_knight,
                    knights_in_dictionary,
                    knight
                )
            )
        )

    return {
        **final_battle(ready_knights[0], ready_knights[2]),
        **final_battle(ready_knights[1], ready_knights[3])
    }


print(battle(knights))
