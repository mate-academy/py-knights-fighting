from app.equipment import Armour, Weapon, Potion
from app.gameplay import Logic, Knight

BATTLE_PAIRS = [
    ("Lancelot", "Mordred"),
    ("Arthur", "Red Knight"),
]


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
        Logic.prepare_to_battle(knight)
        prepared_knights[knight.name] = knight

    lancelot = prepared_knights.get("Lancelot")
    mordred = prepared_knights.get("Mordred")
    arthur = prepared_knights.get("Arthur")
    red_knight = prepared_knights.get("Red Knight")

    # -------------------------------------------------------------------------------
    # BATTLE:

    if lancelot and mordred:
        Logic.fight(lancelot, mordred)

    if arthur and red_knight:
        Logic.fight(arthur, red_knight)

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in prepared_knights.values()
    }
