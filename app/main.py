from __future__ import annotations
from app.people.knight import Knight
from app.event.load_config import load_config, KNIGHTS
from app.event.championship import Championship


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    load_config(knights_config)

    for knight_instance in Knight.knights_dict.values():
        if isinstance(knight_instance, Knight):
            knight_instance.set_equipment()

    # -------------------------------------------------------------------------------
    # BATTLE:

    championship = Championship()
    championship.duel(Knight.knights_dict.get("Lancelot"),
                      Knight.knights_dict.get("Mordred"))
    championship.duel(Knight.knights_dict.get("Arthur"),
                      Knight.knights_dict.get("Red Knight"))

    return championship.statistics()


print(battle(KNIGHTS))
