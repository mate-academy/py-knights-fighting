def battle(warriors):
    # make configurations
    battle_result = warriors

    lancelot = warriors["Lancelot"]
    artur = warriors["Artur"]
    mordred = warriors["Mordred"]
    red_knight = warriors["Red Knight"]

    # battle
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    artur.hp -= red_knight.power - artur.protection
    red_knight.hp -= artur.power - red_knight.protection

    # check if alive
    for key, values in warriors.items():
        if values.hp <= 0:
            values.hp = 0
        warriors[key] = values.hp
    return battle_result
