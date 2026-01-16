from app.preparation.config_knight import config_knight
from app.battle.fight import fighting
from app.knights_variable import KNIGHTS


def battle(fighters: dict) -> dict:
    # Preparation
    creation = config_knight(fighters)

    # Battle
    fighting(creation)

    # Return battle results:
    return {
        creation[knight]["name"]: creation[knight]["hp"] for knight in creation
    }


print(battle(KNIGHTS))
