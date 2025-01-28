from app.knights.knights_store import KNIGHTS
from app.knights.knight import Knight
from app.knights.potion import Potion
from app.actions.duel import duel


def battle(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:
    knights_for_fight = {}

    for knight_alias, knight_data in knights_config.items():
        knights_for_fight.update(
            {knight_alias: (
                Knight(
                    knight_data["name"],
                    knight_data["power"],
                    knight_data["hp"],
                    knight_data["armour"],
                    knight_data["weapon"],
                    (Potion(
                        knight_data["potion"]["name"],
                        knight_data["potion"]["effect"])
                        if knight_data["potion"]
                        else None)))})

    # BATTLE:
    duel(knights_for_fight["lancelot"], knights_for_fight["mordred"])
    duel(knights_for_fight["red_knight"], knights_for_fight["arthur"])

    # Return battle results:
    return {knight.name: knight.hp for knight in knights_for_fight.values()}


print(battle(KNIGHTS))
