def conduct_battle(knight1, knight2):
    battle_result = {
        knight1.name: calculate_hp_loss(knight1, knight2),
        knight2.name: calculate_hp_loss(knight2, knight1)
    }
    return battle_result


def calculate_hp_loss(attacker, defender):
    hp_loss = attacker.power - defender.protection
    if hp_loss < 0:
        hp_loss = 0
    return hp_loss
