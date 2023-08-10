from app.Knights import Knight
from app.battle import Battle
from app.knights_data import KNIGHTS


def battle(knigts: dict) -> dict:
    knigts_fighters: dict[str, Knight] = Knight.create_dict_of_knghtes(knigts)

    Battle.make_fight(knigts_fighters)
    Battle.is_anyone_alive(knigts_fighters)

    return Battle.return_result(knigts_fighters)


battle(KNIGHTS)
