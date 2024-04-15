from app.knight import Knight


def battle(knightsconfig: any) -> any:
    lancelot = Knight(**knightsconfig["lancelot"])
    arthur = Knight(**knightsconfig["arthur"])
    mordred = Knight(**knightsconfig["mordred"])
    red_knight = Knight(**knightsconfig["red_knight"])

    # Apply armour, weapon, and potion effects for each knight
    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    # BATTLE:
    lancelot_hp = max(0, lancelot.hp - (mordred.power - lancelot.protection))
    mordred_hp = max(0, mordred.hp - (lancelot.power - mordred.protection))
    arthur_hp = max(0, arthur.hp - (red_knight.power - arthur.protection))
    red_knight_hp = max(0, red_knight.hp - (arthur.power
                                            - red_knight.protection))

    return {
        lancelot.name: lancelot_hp,
        arthur.name: arthur_hp,
        mordred.name: mordred_hp,
        red_knight.name: red_knight_hp,
    }
