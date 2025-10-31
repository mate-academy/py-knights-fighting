from app.equipment import Armour, Weapon, Potion
from app.gameplay import Logic, Knight


def battle(knights_config: dict) -> dict:

    prepared_knights = {}

    for key, config in knights_config.items():
        # creating equipment classes instance
        armour_obj = (
            Armour(config.get("armour"))
            if config.get("armour")
            else None
        )
        weapon_data = config.get("weapon")
        weapon_obj = (
            Weapon(weapon_data["name"], weapon_data["power"])
            if weapon_data
            else None
        )
        potion_data = config.get("potion")

        potion_obj = (
            Potion(potion_data["name"], potion_data["effect"])
            if potion_data
            else None
        )

        # creating knight instance
        knight = Knight(
            config["name"],
            config["power"],
            config["hp"],
            armour_obj,
            weapon_obj,
            potion_obj
        )
        prepared_knights[knight.name] = knight

    prepared_lancelot = prepared_knights.get("Lancelot")
    prepared_arthur = prepared_knights.get("Arthur")
    prepared_mordred = prepared_knights.get("Mordred")
    prepared_red_knight = prepared_knights.get("Red Knight")

    # apply armour, apply weapon, apply potion if exist
    Logic.prepare_to_battle(prepared_lancelot)
    Logic.prepare_to_battle(prepared_arthur)
    Logic.prepare_to_battle(prepared_mordred)
    Logic.prepare_to_battle(prepared_red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    Logic.fight(prepared_lancelot, prepared_mordred)

    # 2 Arthur vs Red Knight:
    Logic.fight(prepared_arthur, prepared_red_knight)

    # Return battle results:
    return {
        prepared_lancelot.name: prepared_lancelot.hp,
        prepared_arthur.name: prepared_arthur.hp,
        prepared_mordred.name: prepared_mordred.hp,
        prepared_red_knight.name: prepared_red_knight.hp,
    }
