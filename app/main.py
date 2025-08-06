from app.battle_preparation.preparation import battle_preparation


def battle(dictionary: dict) -> dict[str, int]:
    correct_order = ["Lancelot", "Arthur", "Mordred", "Red Knight"]
    result_of_battle = {}
    list_of_rk = battle_preparation(dictionary)
    for i, obj in enumerate(correct_order):
        list_of_rk[obj].hp -= list_of_rk[correct_order[i - 2]
                                         ].power - list_of_rk[obj].protection
        result_of_battle[list_of_rk[obj].name] = list_of_rk[obj].hp
    for knight, hp in result_of_battle.items():
        if hp < 0:
            result_of_battle[knight] = 0
    return result_of_battle
