from app.knights import Knight


def battle(knights_config: dict) -> dict[int]:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    members_of_fight = [lancelot, arthur, mordred, red_knight]

    for knight in members_of_fight:
        knight.apply_weapon()
        knight.apply_potion()

    damage_lancelot_to_mordred = lancelot.attack(mordred)
    damage_mordred_to_lancelot = mordred.attack(lancelot)
    lancelot.take_damage(damage_mordred_to_lancelot)
    mordred.take_damage(damage_lancelot_to_mordred)

    damage_arthur_to_red_knight = arthur.attack(red_knight)
    damage_red_knight_to_arthur = red_knight.attack(arthur)
    arthur.take_damage(damage_red_knight_to_arthur)
    red_knight.take_damage(damage_arthur_to_red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
