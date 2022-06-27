from app.knights_configuration import configured_knights

#
def battle(knights):

    # 1 Lancelot vs Mordred:

    lancelot = knights["lancelot"]
    print(lancelot)
    mordred = knights["mordred"]

    lancelot.versus(mordred)

    # 2 Arthur vs Red Knight:

    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    arthur.versus(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(configured_knights))
