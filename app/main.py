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
        # preparing knight to battle
        Logic.prepare_to_battle(knight)

        # saving prepared knight
        prepared_knights[knight.name] = knight

    # -------------------------------------------------------------------------------
    # BATTLE:

    for name_a, name_b in BATTLE_PAIRS:
        fighter_a = prepared_knights.get(name_a)
        fighter_b = prepared_knights.get(name_b)

    # Checking if exist
        if fighter_a and fighter_b:
            Logic.fight(fighter_a, fighter_b)

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in prepared_knights.values()
    }
