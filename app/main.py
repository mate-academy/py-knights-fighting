from app.battle_preparation.preparation import battle_preparation


def battle(dictionary: dict) -> dict:
    result_of_battle = {}
    list_of_rk = battle_preparation(dictionary)
    for i in range(0, len(list_of_rk)):
        list_of_rk[i].hp -= list_of_rk[i - 2].power - list_of_rk[i].protection
        result_of_battle[list_of_rk[i]] = list_of_rk[i].hp
    for knight, hp in result_of_battle.items():
        if hp < 0:
            result_of_battle[knight] = 0
    return result_of_battle
