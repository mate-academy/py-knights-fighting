from .preparations import preparations as prepare


def fights(config: dict) -> dict:
    prepare_knights_list = prepare(config)

    # make Knight object
    lancelot = prepare_knights_list.get("Lancelot")
    arthur = prepare_knights_list.get("Artur")
    mordred = prepare_knights_list.get("Mordred")
    red_knight = prepare_knights_list.get("Red Knight")

    # battle 1
    lancelot.hp -= mordred.power - lancelot.armour
    mordred.hp -= lancelot.power - mordred.armour

    # battle 2
    arthur.hp -= red_knight.power - arthur.armour
    red_knight.hp -= arthur.power - red_knight.armour

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0
    if mordred.hp <= 0:
        mordred.hp = 0
    if arthur.hp <= 0:
        arthur.hp = 0
    if red_knight.hp <= 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
