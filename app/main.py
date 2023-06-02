from app.battle.battle import Battle
from app.battle.commentary import Commentary
from app.battle.preparation import KnightPrep
# from app.knights_data.knights import KNIGHTS  # uncomment to use KNIGHTS file


def battle(knights_config: dict) -> dict:
    Commentary.opening_com()

    knight_objects = {
        knight_name: KnightPrep(*knight_stats.values())
        for knight_name, knight_stats in knights_config.items()
    }

    commentary_objects = []

    for knight in knight_objects.values():
        commentary_objects.append(Commentary(knight))
        KnightPrep.get_ready_for_battle(knight)

    for knight in commentary_objects:
        Commentary.introduction(knight)

    Commentary.before_battle_com()

    Battle.battle(knight_objects["lancelot"], knight_objects["mordred"])
    Commentary.battle_com(knight_objects["lancelot"],
                          knight_objects["mordred"])

    Battle.battle(knight_objects["arthur"], knight_objects["red_knight"])
    Commentary.battle_com(knight_objects["arthur"],
                          knight_objects["red_knight"])

    Commentary.end_com()

    return {
        knight_objects[knight].name: knight_objects[knight].hp
        for knight in knight_objects
    }
