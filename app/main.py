from app.preparation.config_knight import config_knight
from app.battle.fight import battle
from app.knights import KNIGHTS


def fighting(fighters: dict) -> dict:
    # Preparation
    creation = config_knight(fighters)

    # Battle
    battle(creation)

    # Return battle results:
    return {
        creation[knight]["name"]: creation[knight]["hp"] for knight in creation
    }


print(fighting(KNIGHTS))
