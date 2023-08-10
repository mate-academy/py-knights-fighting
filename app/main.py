from app.Knights import Knight
from app.battle import Battle
from app.knights_data import KNIGHTS


def battle(
        knigts: dict[str, Knight],
        knight1: str = "Lancelot",
        knight2: str = "Mordred",
        knight3: str = "Arthur",
        knight4: str = "Red Knight",
) -> dict:
    knigts_fighters: dict[str, Knight] = Knight.create_dict_of_knghtes(knigts)

    Battle.make_fight(knigts_fighters, knight1, knight2)
    Battle.make_fight(knigts_fighters, knight3, knight4)
    Battle.is_anyone_alive(knigts_fighters)

    return Battle.return_result(knigts_fighters)


battle(KNIGHTS)
