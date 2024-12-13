from app.battle_praparation.fight_preparation import fight_preparation
from app.fight import fight
from app.knight.all_knights import all_knights_create


def battle(knights_all: dict) -> dict:
    knights_list = all_knights_create(knights_all)
    for knight in knights_list:
        fight_preparation(knight)
    fight(knights_list[0], knights_list[2])
    fight(knights_list[1], knights_list[3])
    battle_results = {knight.name: max(knight.hp, 0)
                      for knight in knights_list}
    return battle_results
