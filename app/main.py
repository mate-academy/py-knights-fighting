from app.knights import KNIGHTS
from app.knight import Knight


def create_knight(knight: dict) -> Knight:
    return Knight(
        knight["name"],
        knight["power"],
        knight["hp"],
        knight["armour"],
        knight["weapon"],
        knight["potion"]
    )


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # knights
    lancelot = create_knight(knights_config["lancelot"])
    arthur = create_knight(knights_config["arthur"])
    mordred = create_knight(knights_config["mordred"])
    red_knight = create_knight(knights_config["red_knight"])

    # apply armour
    lancelot.apply_armour()
    arthur.apply_armour()
    mordred.apply_armour()
    red_knight.apply_armour()

    # apply weapon
    lancelot.apply_weapon()
    arthur.apply_weapon()
    mordred.apply_weapon()
    red_knight.apply_weapon()

    # apply potion if exist
    lancelot.apply_potion()
    arthur.apply_potion()
    mordred.apply_potion()
    red_knight.apply_potion()

    # -------------------------------------------------------------------------------
    # Return battle results:
    return {
        lancelot.name: lancelot.battle_result_hp(mordred),
        arthur.name: arthur.battle_result_hp(red_knight),
        mordred.name: mordred.battle_result_hp(lancelot),
        red_knight.name: red_knight.battle_result_hp(arthur),
    }


print(battle(KNIGHTS))
