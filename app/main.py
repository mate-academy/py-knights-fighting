from app.Knights.knight_class import Knight


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knight(knightsconfig["lancelot"])
    arthur = Knight(knightsconfig["arthur"])
    mordred = Knight(knightsconfig["mordred"])
    red_knight = Knight(knightsconfig["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    lancelot.knights_buttle(mordred)
    arthur.knights_buttle(red_knight)

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}
