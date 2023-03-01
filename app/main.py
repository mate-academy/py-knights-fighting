from app.arena.preparation import Prepare
from app.arena.fight import Battle


def battle(knights: dict) -> dict:
    fighters_list = []
    battle_result = {}

    for key, value in knights.items():

        key = Prepare(value)
        key.fighter_preparation()
        fighters_list.append(key)

    Battle.fight(fighters_list[0], fighters_list[2])
    Battle.fight(fighters_list[1], fighters_list[3])

    for fighter in fighters_list:
        battle_result[fighter.name] = fighter.hp

    return battle_result
