from app.knights import lancelot, arthur, mordred, red_knight


def battle(lancelot=lancelot,
           arthur=arthur,
           mordred=mordred,
           red_knight=red_knight):

    lancelot.attack_enemy(mordred)
    mordred.attack_enemy(lancelot)

    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    arthur.attack_enemy(red_knight)
    red_knight.attack_enemy(arthur)

    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp,
            }


print(battle(lancelot, arthur, mordred, red_knight))
