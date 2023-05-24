from app.preparation_for_battle.prepare_lancelot import prepare_lancelot
from app.preparation_for_battle.prepare_arthur import prepare_arthur
from app.preparation_for_battle.prepare_mordered import prepare_mordred
from app.preparation_for_battle.prepare_red_knight import prepare_red_knight


def battle() -> dict:
    # Prepare knights
    lancelot = prepare_lancelot()
    arthur = prepare_arthur()
    mordred = prepare_mordred()
    red_knight = prepare_red_knight()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # Check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle())
