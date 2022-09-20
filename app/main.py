from app.preparation import Preparation
from app.battle import Battle


def battle(knights_config):
    knight_list = []
    # Return battle results:
    for knight in knights_config:
        knight = knights_config[f"{knight}"]
        knight_prep = Preparation(knight)
        knight_prep.apply_armour()
        knight_prep.apply_weapon()
        knight_prep.apply_potion_if_exist()
        knight_list.append(knight)

    first_battle = Battle(knight_list[0], knight_list[2])
    first_battle.battle()
    second_battle = Battle(knight_list[1], knight_list[3])
    second_battle.battle()

    return {knight["name"]: knight["hp"] for knight in knight_list}
